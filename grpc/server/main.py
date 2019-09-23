#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import time
import grpc
from concurrent import futures
from proto import hello_pb2, hello_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Greeter(hello_pb2_grpc.HelloWordServicer):
    def Hello(self, request, context):
        return hello_pb2.StringResponse(resp="鸡,你太美!")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor())
    hello_pb2_grpc.add_HelloWordServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:8098')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
