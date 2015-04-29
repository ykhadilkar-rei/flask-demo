from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World Yatin!'

@app.route('/yoo')
def yoo_world():
    return 'Yooo Yatin!'

if __name__ == '__main__':
    app.run()
