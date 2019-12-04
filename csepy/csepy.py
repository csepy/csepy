#!/usr/bin/python3
from csepy.System.EndpointMap.EndpointMapper import CreatePublicEndpointMap
from csepy.System.Models.Context.ContextFactory import GetContext
from os.path import dirname


functionsPackagePaths = []


def Subscribe(path):
    if path:
        functionsPackagePaths.append(path)


def InitAndGetContext(root, functionsPackagePath=None):
    CreatePublicEndpointMap(root, functionsPackagePath)
    context = GetContext()
    return context


def EnqueueAndRun(context, request=""):
    context.Logger.System(f"user input: {request}")
    context.CommandQueue.EnqueueCommands([request])
    context.CommandQueue.RunCommands()


def Start(pathList=None, sysargs=None):
    root = dirname(__file__)
    if pathList and len(pathList) > 0:
        for path in pathList:
            Subscribe(path)
    context = InitAndGetContext(root, functionsPackagePaths)
    if sysargs and len(sysargs) > 1:
        EnqueueAndRun(context, " ".join(sysargs[1:]))
    while True:
        context.Logger.System("Please enter your next command")
        EnqueueAndRun(context, input(""))
