from flask import Flask, jsonify, request

from blueprint import setup_blueprints
from logger import setup_logger

app = Flask(__name__)

if __name__ == '__main__':
    setup_logger()
    setup_blueprints(app)
    app.run(host='0.0.0.0', port=6000, debug=False, threaded=True)
