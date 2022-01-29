from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/Test')
def Test_func():
    return 'Test routing !'


if __name__ == '__main__':
    app.run()