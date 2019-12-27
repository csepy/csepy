#!/usr/bin/python3
from csepy.System.EndpointMap.EndpointMapper import CreatePublicEndpointMap
from csepy.System.Models.Context.ContextFactory import GetContext
from os.path import dirname


class Service:
    functionsPackagePaths = []

    def Subscribe(self, path):
        if path:
            self.functionsPackagePaths.append(path)

    def InitAndGetContext(self, root, functionsPackagePath=None):
        CreatePublicEndpointMap(root, functionsPackagePath)
        context = GetContext()
        return context

    def EnqueueAndRun(self, context, request=""):
        context.Logger.System(f"user input: {request}")
        context.CommandQueue.EnqueueCommands([request])
        context.CommandQueue.RunCommands()

    def Start(self, pathList=None, sysargs=None):
        root = dirname(__file__)
        if pathList and len(pathList) > 0:
            for path in pathList:
                self.Subscribe(path)
        context = self.InitAndGetContext(root, self.functionsPackagePaths)
        if sysargs and len(sysargs) > 1:
            self.EnqueueAndRun(context, " ".join(sysargs[1:]))
        while True:
            context.Logger.System("Please enter your next command")
            self.EnqueueAndRun(context, input(""))
