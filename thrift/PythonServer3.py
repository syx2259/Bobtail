#!/usr/bin/env python

# This server demonstrates Thrift's connection and "oneway" asynchronous jobs
# showCurrentTimestamp : which returns current time stamp from server
# asynchronousJob() : prints something, waits 10 secs and print another string
#

port = 9090

import sys
# your gen-py dir
sys.path.append('../gen-py')

import time

# Example files
from Example import *
from Example.ttypes import *

# Thrift files
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

M = 600000
LOW_MARK = 13
HIGH_MARK = 65

# Server implementation
class ExampleHandler:
    
    # return current time stamp
    def showCurrentTimestamp(self):
        num_delay = 0
        print('Start at: ' + str(time.time()))
        for i in range(M):
            startTime = time.time()
            time.sleep(0.001)
            endTime = time.time()
            if endTime - startTime > 0.01:
                num_delay+=1
        print('End at: ' + str(time.time()))
        return str(num_delay)
    

    # print something to string, wait 10 secs, than print something again
    def asynchronousJob(self):
        print('Assume that this work takes 10 seconds')
        time.sleep(10)
        print('Job finished, but client didn\'t wait for 10 seconds')


# set handler to our implementation
handler = ExampleHandler()

processor = Example.Processor(handler)
transport = TSocket.TServerSocket("0.0.0.0", port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

# set server
server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)

print('Starting server')
server.serve()
