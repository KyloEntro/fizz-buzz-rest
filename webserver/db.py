import logging
import logging.config
from typing import List

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
        return list(self.local.values())

    def insert_stat(self, item: StatItem) -> None:
        if item.key in self.local:
            self.local[item.key]["count"] += 1
        else:
            self.local[item.key] = vars(item)


class MongoDb(Db):
    def __init__(self):
        pass

    def connect(self, ipAddress: str, port: int, username: str, password: str) -> bool:
        return False

    def get_stats(self) -> List[StatItem]:
        return self.local

    def insert_stat(self, item: StatItem) -> None:
        if item.key in self.local:
            self.local[item.key]["limit"] += item.limit
        else:
            self.local[item.key] = vars(item)
