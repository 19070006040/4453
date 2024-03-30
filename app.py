from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    
    return "Hello World"

@app.route('/hello2')
def hello2():
    
    return "Hello World2"

# Merged HelloWorld3
@app.route('/hello3')
def hello3():
    
    return "Hello World3"

if __name__ == '__main__':
    app.run(debug=True)
#efe
