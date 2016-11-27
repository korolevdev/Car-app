from flask import request
from app import *
from wrappers import *
from api_methods import *

@app.route('/hello/', methods=['GET'])
def url_hello():
    response = hello()
    return response_wrap(response)