#!/usr/bin/python3


class CommandLineService():
    def __init__(self, context):
        self.context = context

    def Run(self, sysargs):
        if sysargs and len(sysargs) > 1:
            self.EnqueueAndRun(self.context, " ".join(sysargs[1:]))
        while True:
            self.context.Logger.System("Please enter your next command")
            self.EnqueueAndRun(self.context, input(""))

    def EnqueueAndRun(self, context, request=""):
        context.Logger.System(f"user input: {request}")
        context.CommandQueue.EnqueueCommands([request])
        context.CommandQueue.RunCommands()

