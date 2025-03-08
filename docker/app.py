from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello,! This is a simple Flask app running in Docker with image3:1.2."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
