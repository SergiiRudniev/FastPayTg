import pymongo
import redis

class Database:
    def __init__(self, mongo_uri, redis_host, redis_port):
        self.mongo_client = pymongo.MongoClient(mongo_uri)
        self.mongo_db = self.mongo_client.get_database()
        self.redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

    def create_user(self, user_id, balance):
        try:
            user_data = {'_id': user_id, 'balance': balance}
            self.mongo_db.users.insert_one(user_data)
            return True
        except:
            return False
    def get_balance(self, user_id):
        balance_cached = self.redis_client.get(user_id)
        if balance_cached is not None:
            return float(balance_cached)

        user_data = self.mongo_db.users.find_one({'_id': user_id})
        if user_data:
            balance = user_data['balance']
            self.redis_client.setex(user_id, 60, balance)
            return balance
        else:
            return None

    def update_balance(self, user_id, new_balance):
        self.mongo_db.users.update_one({'_id': user_id}, {'$set': {'balance': new_balance}})
        ttl = self.redis_client.ttl(user_id)
        self.redis_client.setex(user_id, ttl, new_balance)

    def clear_cache(self, user_id=None):
        if user_id:
            self.redis_client.delete(user_id)
        else:
            self.redis_client.flushall()

    def close_connections(self):
        self.mongo_client.close()
        self.redis_client.close()
