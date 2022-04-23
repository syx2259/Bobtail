#!/usr/bin/env python

# This client demonstrates Thrift's connection and "oneway" asynchronous jobs
# Client connects to server host:port and calls 2 methods
# showCurrentTimestamp : which returns current time stamp from server
# asynchronousJob() : which calls a "oneway" method
#

# host = "localhost"
# port = 9090

from asyncio import futures
import sys
import time
from concurrent.futures import ThreadPoolExecutor

# your gen-py dir
sys.path.append('../gen-py')

# Example files
from Example import *
from Example.ttypes import *

# Thrift files
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def requestOne(host, port, index):
    transport = TSocket.TSocket(host, port)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Example.Client(protocol)
    transport.open()
    if index == 0:
        f = open("goodNode.txt", "w")
        #f = open("badNode.txt", "w")
        bobtailResult = client.showCurrentTimestamp()
        f.write(bobtailResult + "\n")
        f.close()
    else :
        # Run showCurrentTimestamp() method on server
        bobtailResult = client.showCurrentTimestamp()
    transport.close()
    return "Finish work in " + host

def requestAll(hosts):
    futures_list = []
    results = []
    with ThreadPoolExecutor(max_workers=6) as executor:
        index = 0
        for host in hosts:
            futures = executor.submit(requestOne, host, 9090, index)
            futures_list.append(futures)
    
        for future in futures_list:
            try:
                result = future.result(timeout=60)
                results.append(result)
            except Exception:
                results.append(None)
    return results

if __name__ == "__main__":
    try:
        #Good node test
#         hosts = ("10.0.2.21", "10.0.2.22", "10.0.2.23", "10.0.2.24", "10.0.2.25")
#         results = requestAll(hosts)
#         for result in results:
#             print(result)

        #Bad node test
        result = requestOne("10.0.2.21", 9090, 0)
        print(result)
    except Thrift.TException as tx:
        print('Something went wrong : %s' % (tx.message))
