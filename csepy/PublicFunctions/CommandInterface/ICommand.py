#!/usr/bin/python3
import abc
from csepy.PublicFunctions.ShellCommands.ShellCommandExecutor.ShellCommandExecutor import RunSubProcess


class ICommand(metaclass=abc.ABCMeta):
    def __init__(self, request, context):
        self.request = request
        self.context = context

    @abc.abstractmethod
    def Execute(self):
        pass

    def PreExecute(self):
        self.context.Logger.DEBUG(f"Running command '{self.PublicFacing}' with parameters {str(self.request)}")
        if self.request and len(self.request) > 0 and "--help" in self.request:
            self.RunHelpCommand(self.context, self.Help)
            return False
        if not self.ValidateRequestContainsMinimumRequiredParameters(self.MinRequestParameters):
            self.context.Logger.WARN(f"Missing required parameters (min amount: {self.MinRequestParameters})")
            return False
        return True

    def RunShellCommand(self, command):
        RunSubProcess(command, self.context.Logger)

    def ValidateRequestContainsMinimumRequiredParameters(self, minParams=0):
        requestHasAtLeastMinRequiredParams = True if (minParams == 0) or (
                self.request and len(self.request) >= minParams) else False
        return requestHasAtLeastMinRequiredParams

    def RunHelpCommand(self, help):
        self.context.Logger.INFO('\t\t'.join(('\t\t' + help.lstrip()).splitlines(True)))

