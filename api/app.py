import logging

from flask import Flask, request
from flask_cors import CORS
from twilio import twiml

app = Flask(__name__)
CORS(app)


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    logging.info(data)

    resp = twiml.Response()
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)


if __name__ == "__main__":
    app.run()
