#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import grpc
from proto import hello_pb2, hello_pb2_grpc


def client():
    channel = grpc.insecure_channel('localhost:8098')
    stub = hello_pb2_grpc.HelloWordStub(channel)
    response = stub.Hello(hello_pb2.StringRequest(param="cxk"))
    print("Response message:", response.resp)


if __name__ == '__main__':
    client()
