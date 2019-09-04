import os
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World...again"


app.run(host=os.environ.get('IP', '127.0.0.1'),
        port=int(os.environ.get('PORT', '8080')),
        debug=True)
