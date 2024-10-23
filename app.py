import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Version Two!'

@app.route('/secret/')
def secret():
    return 'Secret password xyzzy'

if __name__ == '__main__':
    app.run()
