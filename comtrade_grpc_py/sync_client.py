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
import comtrade_pb2
import comtrade_pb2_grpc
import arrow
import comtrade_grpc
import os

CHANNEL_OPINIONS=[
    ('grpc.max_receive_message_length',999999999)
]

base_dir = os.path.split(os.path.abspath(__file__))[0]  

cfg_file = f'{base_dir}/38957.cfg_utf8.cfg'
dat_file = f'{base_dir}/38957.dat'

def run() -> None:
    with grpc.insecure_channel('localhost:50051',options=CHANNEL_OPINIONS) as channel:
        stub = comtrade_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(comtrade_pb2.HelloRequest(name='you'))
        print("Greeter client received: " + response.message)
        print(arrow.now())
        response = stub.TestFastLoad(comtrade_pb2.HelloRequest(name="fast"))
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
    a=arrow.now()
    print('0ms')
    print("rec = comtrade_grpc.Comtrade(grpc_endpoint='localhost:50051')\nrec.load(cfg_file,dat_file)")
    rec = comtrade_grpc.Comtrade(grpc_endpoint='localhost:50051')
    rec.load(cfg_file,dat_file)
    b=arrow.now()
    print(f'{(b-a).total_seconds()*1000}ms')
    print("rec = comtrade_grpc.Comtrade()\nrec.load(cfg_file,dat_file)")
    rec = comtrade_grpc.Comtrade()
    rec.load(cfg_file,dat_file)
    c=arrow.now()
    print(f'{(c-a).total_seconds()*1000}ms')


if __name__ == '__main__':
    logging.basicConfig()
    # asyncio.run(run())
    run()
    run_load()