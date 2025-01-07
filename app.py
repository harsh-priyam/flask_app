from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a Flask app running via AWS App Runner!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
