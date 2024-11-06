# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Changed main.py file!!!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
