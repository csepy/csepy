#!/usr/bin/python3
import sys
from csepy.csepy import Start


if len(sys.argv) > 1:
    Start(sys.argv)
elif __name__ == '__main__':
    Start()
