from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    msg = os.getenv("GREETING_MESSAGE", "Hello this is image2 with version 5.0")
    return f"<h4>{msg}</h4>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005)