#!/usr/bin/python3
import sys
from csepy.csepy import Service


# service = Service("commandLine")
service = Service("server")
service.SetHostAndPort("localhost", 8000)
if len(sys.argv) > 1:
    service.Start(sysargs=sys.argv)
elif __name__ == '__main__':
    service.Start()
