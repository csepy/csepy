#!/usr/bin/python3
import sys
from csepy.csepy import Start
from csepy.System.Server.HttpRequestHandler import Listen


if len(sys.argv) > 1:
    Listen()
#     Start(sysargs=sys.argv)
elif __name__ == '__main__':
    Listen()
#     Start()
