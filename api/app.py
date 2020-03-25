import hashlib
import logging

from flask import Flask, request
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse

from .database import POSITIVELY_FAKE

app = Flask(__name__)
CORS(app)


@app.route("/check", methods=["POST"])
def check():
    data = dict(request.values)
    app.logger.info(data)
    msg = data.get("Body")
    msg_hash = hashlib.md5(msg.encode()).hexdigest()

    if msg_hash in POSITIVELY_FAKE:
        app.logger.info(f"->FAKE_NEWS_FOUND<- hash={msg_hash} msg={msg}",)

        resp = MessagingResponse()
        resp.message(
            "Oops, this is *positively FAKE NEWS*. "
            "Please let the original sender know about this."
        )
        return str(resp)
    else:
        app.logger.error(f"->ENTRY_NOT_FOUND<- hash={msg_hash} msg={msg}",)
        resp = MessagingResponse()
        resp.message(
            "I was unable to verify this, so I'll have a human take a look. "
            "Please try again in a couple of hours."
        )
        return str(resp)


if __name__ == "__main__":
    app.run()
else:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
