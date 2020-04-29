import redis
import fakeredis


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


class MockDatabase(Database):

    def __init__(self, is_connected):
        super().__init__()
        self.r_server = fakeredis.FakeServer()
        self.r_server.connected = is_connected
        self.fake_redis = fakeredis.FakeStrictRedis(server=self.r_server)
        self.is_connected = is_connected

    def connect(self):
        return self.is_connected
