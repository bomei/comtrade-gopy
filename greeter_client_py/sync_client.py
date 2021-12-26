# Copyright 2020 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python AsyncIO implementation of the GRPC helloworld.Greeter client."""

import asyncio
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc
import arrow
from comtrade_grpc import Comtrade,Cfg
import os

CHANNEL_OPINIONS=[
    ('grpc.max_receive_message_length',999999999)
]


cfg_file = r'C:\tools\Go\src\bomei\comtrade-gopy\greeter_client_py\38957.cfg_utf8.cfg'
dat_file = r'C:\tools\Go\src\bomei\comtrade-gopy\greeter_client_py\38957.dat'

def run() -> None:
    with grpc.insecure_channel('localhost:50051',options=CHANNEL_OPINIONS) as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)
        print(arrow.now())
        response = stub.TestFastLoad(helloworld_pb2.HelloRequest(name="fast"))
        a=[]
        for ch in response.channel:
            b=[]
            for i in ch.value:
                b.append(i)
            a.append(b)
        # print(a[0][0])
        print(arrow.now())
        # print(a[0])

def run_load()->None:
    print(arrow.now())
    rec = Comtrade(grpc_endpoint='localhost:50051')
    rec.load(cfg_file,dat_file)
    print(arrow.now())
    print(rec.analog[0])



if __name__ == '__main__':
    logging.basicConfig()
    # asyncio.run(run())
    run()
    run_load()