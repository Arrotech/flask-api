import os
import socket

from flask import make_response, jsonify

from app import create_app


app = create_app(os.environ.get('FLASK_ENV', default='development'))


@app.route('/')
def home():
    return make_response(jsonify({
        "message": "It works",
        "status": "200",
        "host": socket.gethostname(),
    }), 200)


if __name__ == '__main__':
    app.run()
