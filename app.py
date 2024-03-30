from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    data = get_data_from_database()
    return f'Hello, World! Here is some data from the database: {data}'

if __name__ == '__main__':
    app.run(debug=True)
#efe
