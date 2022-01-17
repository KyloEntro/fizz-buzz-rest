import logging
import logging.config
from typing import List
import pymongo
import json

logging.config.fileConfig('logging.conf')
logger = logging.getLogger('root')


class StatItem:
    def __init__(self, int1: int, str1: str, int2: int, str2: str, limit: int, count: int = 1):
        self.key = f"{int1}-{str1}-{int2}-{str2}-{limit}"
        self.int1 = int1
        self.str1 = str1
        self.int2 = int2
        self.str2 = str2
        self.limit = limit
        self.count = count


class Db:
    def connect(self, ipAddress: str, port: int, username: str, password: str) -> bool:
        pass

    def get_stats(self) -> List[StatItem]:
        pass

    def insert_stat(self, item: StatItem) -> None:
        pass


class LocalDb(Db):
    def __init__(self):
        self.local = {}

    def connect(self, ipAddress: str, port: int, username: str, password: str) -> bool:
        logger.info("Local DB connected")
        return True

    def get_stats(self) -> List[StatItem]:
        result = []
        for d in self.local.values():
            result.append(
                StatItem(d['int1'], d['str1'], d['int2'], d['str2'], d['limit'], d['count']))
        return result

    def insert_stat(self, item: StatItem) -> None:
        if item.key in self.local:
            self.local[item.key]["count"] += 1
        else:
            self.local[item.key] = vars(item)


class MongoDb(Db):
    def __init__(self):
        self.client = None
        self.mydb = None
        self.statCol = None

    def connect(self, ipAddress: str, port: int, username: str, password: str) -> bool:
        self.client = pymongo.MongoClient(f"mongodb://{ipAddress}:{port}")
        try:
            # Try to get server info, if client is not connected to valid mongo server, it will raise an exception
            self.client.server_info()
        except Exception as e:
            logger.warning(f"Can not connect to mongodb server, error => {e}")
            self.client = None
            return False

        self.mydb = self.client["fizzbuzz"]
        self.statCol = self.mydb["statistic"]
        logger.info(f"Mongo server connected")
        return True

    def get_stats(self) -> List[StatItem]:
        result = []
        if self.statCol is not None:
            datas = self.statCol.find()
            for d in datas:
                result.append(
                    StatItem(d['int1'], d['str1'], d['int2'], d['str2'], d['limit'], d['count']))
        else:
            logger.error("Error in connection to mongo database server")
        return result

    def insert_stat(self, item: StatItem) -> None:
        if self.statCol is not None:
            found = self.statCol.find_one({'key': item.key})
            print(found)

            if found is None:
                self.statCol.insert_one(vars(item))
            else:
                newCount = item.count + found['count']
                self.statCol.update_one({"key": found['key']}, {
                                        "$set": {"count": newCount}})

        else:
            logger.error("Error in connection to mongo database server")
            raise Exception("Error in insertion, can not connect to database")

        """
        data = json.dumps(vars(item))  # Transform to json data
        print(data)
        if item.key in self.local:
            self.local[item.key]["limit"] += item.limit
        else:
            self.local[item.key] = vars(item)
        """
