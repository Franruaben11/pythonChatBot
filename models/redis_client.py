import redis
from flask import session

from config import CONNECT_REDIS

r = redis.Redis(**CONNECT_REDIS)

class RedisClient:

    def __init__(self):
        self.r = redis.Redis(**CONNECT_REDIS)

    def save_user_message(self, user_id, message):
        self.r.rpush(f"chat:{user_id}", f"usuario: {message}")

    def save_ai_message(self, user_id, message):
        self.r.rpush(f"chat:{user_id}", f"ai: {message}")

    def get_last_12_msg(self, user_id):
        msgs = self.r.lrange(f"chat:{user_id}", -12, -1)
        return [msg.decode() for msg in msgs]

    def get_all_msg(self, user_id):
        msgs = self.r.lrange(f"chat:{user_id}", 0, -1)
        return [msg.decode() for msg in msgs]

    def clear_chat(self, user_id):
        self.r.delete(f"chat:{user_id}")


db_redis = RedisClient()
print(db_redis.get_all_msg("pepe"))