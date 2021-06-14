import os

from flask import make_response, jsonify

from app import create_app


app = create_app(os.environ.get('FLASK_ENV'))


@app.route('/')
def home():
    return make_response(jsonify({
        "message": "OK",
        "status": "200"
    }), 200)


if __name__ == '__main__':
    app.run()
