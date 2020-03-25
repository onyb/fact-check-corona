import logging

from flask import Flask, request
from flask_cors import CORS
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
CORS(app)


@app.route("/check", methods=["POST"])
def check():
    app.logger.info(request.values)
    app.logger.info(request)

    resp = MessagingResponse()
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)


if __name__ == "__main__":
    app.run()
else:
    gunicorn_logger = logging.getLogger("gunicorn.error")
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
