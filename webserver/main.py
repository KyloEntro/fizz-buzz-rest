from crypt import methods
from json.tool import main
from flask import Flask
from flask_cors import CORS
from waitress import serve
import logging
import logging.config
import os

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')
app = Flask(__name__)

# Allow all CORS
CORS(app)


@app.route("/fizzbuzz/<int:int1>/<string:str1>/<int:int2>/<string:str2>/<int:limit>", methods=['GET'])
def fizzbuzz(int1: int, str1: str, int2: int, str2: str, limit: int):
    logger.info(
        f"New request with param : int1 => {int1}; str1 => {str1}; int2 => {int2}; str2 => {str2}; limit => {limit}")

    result = ""

    for index in range(1, limit + 1):
        if index % int1 == 0:
            result += str1
        if index % int2 == 0:
            result += str2

        if index % int1 != 0 and index % int2 != 0:
            result += str(index)

        if index != limit:
            result += ','

    logger.debug(f"Result value => {result}")
    return result


@app.route("/statistic", methods=['GET'])
def get_statistic():
    logger.info(f"New request to get statistic")

    return "Hello"


if __name__ == "__main__":
    # Get IP address and port from system environment variable
    IP_ADDRESS = os.getenv("IP_ADDRESS") if os.getenv(
        "IP_ADDRESS") is not None else "0.0.0.0"
    PORT = os.getenv("PORT") if os.getenv("PORT") is not None else "8080"

    logger.info(
        f"Start to serve the application with ip = {IP_ADDRESS} and port = {PORT}")
    serve(app, host=IP_ADDRESS, port=PORT)
