from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    user = {'name':'Paul'}
    return 'Hello '+user['name']+'!'


if __name__ == '__main__':
    app.run()
