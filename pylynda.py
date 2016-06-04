from flask import Flask

from static.common.database import Database

app = Flask(__name__)

@app.before_first_request
def dbLink():
    Database.initialize()

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
