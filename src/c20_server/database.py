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

    def initialize_user_ids(self):
        if self.r_database.get('user_id') is None:
            self.r_database.set('user_id', 0)

    def set_new_user_id(self, id_number):
        self.r_database.set('user_id', id_number)

    def get_new_user_id(self):
        prev_user_id = self.r_database.get('user_id')
        user_id = prev_user_id + 1
        return user_id


class MockDatabase(Database):

    def __init__(self, is_connected):
        super().__init__()
        self.r_server = fakeredis.FakeServer()
        self.r_server.connected = is_connected
        self.fake_redis = fakeredis.FakeStrictRedis(server=self.r_server)
        self.is_connected = is_connected

    def connect(self):
        return self.is_connected
