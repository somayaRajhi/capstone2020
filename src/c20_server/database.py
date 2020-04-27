import redis


class Database:

    def __init__(self):
        self.r_database = None

    def connect(self):
        try:
            self.r_database = redis.Redis()
            self.r_database.ping()
            return True
        except redis.exceptions.ConnectionError:
            return False
