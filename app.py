
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/hello2')
def hello2():
    return "Hello World2"

@app.route('/hello3')
def hello3():
    return "Hello World3.2"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Ensure the app runs on port 80
