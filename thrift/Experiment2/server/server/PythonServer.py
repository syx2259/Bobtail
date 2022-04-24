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

LOW_MARK = 13
HIGH_MARK = 65

# Server implementation
class ExampleHandler:
    
    # return current time stamp
    def showCurrentTimestamp(self):
        timeStamp = time.time()
        #Bobtail algorithm
        num_delay = 0
        t_start = time.time()
        t_end = t_start + 900
        print('Start at: ' + str(t_start))
        while time.time() < t_end:
            startTime = time.time()
            time.sleep(0.001)
            endTime = time.time()
            if endTime - startTime > 0.01:
                num_delay+=1
                print(num_delay)
        print('End at: ' + str(t_end))
        if num_delay <= LOW_MARK:
            print('GOOD')
            return str(timeStamp)
        elif num_delay <= HIGH_MARK:
            print('MAY USE NETWORK TEST')
            return str(timeStamp)
        print('BAD')
        return str(timeStamp)
    

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
