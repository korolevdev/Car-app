from flask import jsonify

OK = 0

def response_wrap(response, code=OK):
    return jsonify({
        'code': code,
        'response': response
        })