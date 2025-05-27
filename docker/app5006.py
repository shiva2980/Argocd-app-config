from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    msg = os.getenv("GREETING_MESSAGE", "Hello this is image1 with version 4.0")
    return f"<h3>{msg}</h3>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)    