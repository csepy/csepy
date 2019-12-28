#!/usr/bin/python3
from csepy.System.EndpointMap.EndpointMapper import CreatePublicEndpointMap
from csepy.System.Models.Context.ContextFactory import GetContext
from os.path import dirname
from csepy.System.ServiceRunners.Server.HttpRequestHandler import ServerService
from csepy.System.ServiceRunners.CommandLine import CommandLineService


class Service:
    functionsPackagePaths = []

    def __init__(self, serviceType):
        self.serviceType = str.lower(serviceType)
        self.host = ""
        self.port = 0

    def Subscribe(self, path):
        if path:
            self.functionsPackagePaths.append(path)

    def SetHostAndPort(self, host, port):
        self.host = host
        self.port = port

    def InitAndGetContext(self, root, functionsPackagePath=None):
        CreatePublicEndpointMap(root, functionsPackagePath)
        context = GetContext()
        return context

    def GetServiceRunner(self, context):
        serviceRunner = None
        if self.serviceType == "commandline":
            serviceRunner = CommandLineService(context)
        elif self.serviceType == "server":
            serviceRunner = ServerService(context, self.host, self.port)
        return serviceRunner

    def Start(self, pathList=None, sysargs=None):
        root = dirname(__file__)
        if pathList and len(pathList) > 0:
            for path in pathList:
                self.Subscribe(path)
        context = self.InitAndGetContext(root, self.functionsPackagePaths)
        serviceRunner = self.GetServiceRunner(context)
        serviceRunner.Run(sysargs)