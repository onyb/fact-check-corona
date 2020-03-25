from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/check", methods=["POST"])
def check():
    data = request.get_json()
    return jsonify({"content": data})


if __name__ == "__main__":
    app.run()
