import grpc
import concurrent.futures
import db_pb2, db_pb2_grpc
from DataBase import Database
import logging

logger = logging.getLogger(__name__)

mongo_uri = 'mongodb://mongodb:27017/'
redis_host = 'redis'
redis_port = 6379
db = Database(mongo_uri, redis_host, redis_port)

def run_server():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    db_pb2_grpc.add_dbServicer_to_server(dbServicer(), server)
    server.add_insecure_port('0.0.0.0:5040')
    server.start()
    server.wait_for_termination()

class dbServicer(db_pb2_grpc.db):
    def CreateNewUser(self, request, context, **kwargs):
        user_id = request.Id
        status = db.create_user(user_id, 100)
        return db_pb2.DBResponseCreateNewUser(Status=status)

    def GetBalance(self, request, context, **kwargs):
        try:
            status = True
            balance = db.get_balance(request.Id)
        except:
            status = False
            balance = 0
        return db_pb2.DBResponseGetBalance(Status=status, Balance=balance)
if __name__ == '__main__':
    run_server()
