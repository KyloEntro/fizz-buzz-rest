from crypt import methods
from json.tool import main
from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve
import logging
import logging.config
import os
import db

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')
app = Flask(__name__)

# Allow all CORS
CORS(app)

database: db.Db = None


@app.route("/fizzbuzz/<int:int1>/<string:str1>/<int:int2>/<string:str2>/<int:limit>", methods=['GET'])
def fizzbuzz(int1: int, str1: str, int2: int, str2: str, limit: int):
    logger.info(
        f"New request with param : int1 => {int1}; str1 => {str1}; int2 => {int2}; str2 => {str2}; limit => {limit}")

    result = []

    for index in range(1, limit + 1):
        resultStr = ""
        if index % int1 == 0:
            resultStr += str1
        if index % int2 == 0:
            resultStr += str2

        if len(resultStr) == 0:
            resultStr = str(index)

        result.append(resultStr)

    if database is not None:
        database.insert_stat(db.StatItem(int1, str1, int2, str2, limit))

    logger.debug(f"Result value => {result}")
    return jsonify(result)


@app.route("/statistic", methods=['GET'])
def get_statistic():
    logger.info(f"New request to get statistic")
    result = database.get_stats()
    print(result)
    return jsonify(result)


def connect_database(ip, port, username, password) -> db.Db:
    result = db.MongoDb()
    if result.connect(ip, port, username, password):
        return result
    else:
        logger.info(f"MongoDB is not connected, use local storage")
        return db.LocalDb()


if __name__ == "__main__":
    # Get IP address and port from system environment variable
    IP_ADDRESS = os.getenv("IP_ADDRESS") if os.getenv(
        "IP_ADDRESS") is not None else "0.0.0.0"
    PORT = int(os.getenv("PORT")) if os.getenv("PORT") is not None else 8080

    # Get Database information
    DB_IP_ADDRESS = os.getenv("DB_IP_ADDRESS") if os.getenv(
        "DB_IP_ADDRESS") is not None else "127.0.0.1"
    DB_PORT = int(os.getenv("DB_PORT")) if os.getenv(
        "DB_PORT") is not None else 27017
    DB_USERNAME = os.getenv("DB_USERNAME") if os.getenv(
        "DB_USERNAME") is not None else ""
    DB_PASSWORD = os.getenv("DB_USERNAME") if os.getenv(
        "DB_USERNAME") is not None else ""

    database = connect_database(
        DB_IP_ADDRESS, DB_PORT, DB_USERNAME, DB_PASSWORD)

    logger.info(
        f"Start to serve the application with ip = {IP_ADDRESS} and port = {PORT}")
    serve(app, host=IP_ADDRESS, port=PORT)
