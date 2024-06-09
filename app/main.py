import grpc
import db_pb2, db_pb2_grpc
import cProfile


def run_client():
    channel = grpc.insecure_channel('localhost:5040')
    stub = db_pb2_grpc.dbStub(channel)

    request = db_pb2.DBRequestCreateNewUser(Id="id")
    response = stub.CreateNewUser(request)
    print("Результат:", response.Status)

    request = db_pb2.DBRequestGetBalance(Id="id")
    response = stub.CreateNewUser(request)

    print("Результат:", response.Status)

if __name__ == '__main__':
    cProfile.run('run_client()')
