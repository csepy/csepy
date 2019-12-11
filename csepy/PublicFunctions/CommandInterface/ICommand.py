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

        if self.HelpCommandRequested():
            self.RunHelpCommand()
            return False

        if not self.RequestHasMinRequiredParameters():
            return False

        return True

    def RunShellCommand(self, command):
        RunSubProcess(command, self.context.Logger)

    def RequestHasMinRequiredParameters(self):
        minParametersForRequest = self.MinRequestParameters if hasattr(self, "MinRequestParameters") else 0
        requestHasAtLeastMinRequiredParams = (minParametersForRequest == 0) or (
                self.request and len(self.request) >= minParametersForRequest)
        if not requestHasAtLeastMinRequiredParams:
            self.context.Logger.WARN(f"Missing required parameters (min amount: {minParametersForRequest})")
        return requestHasAtLeastMinRequiredParams

    def HelpCommandRequested(self):
        return self.request and len(self.request) > 0 and "--help" in self.request

    def RunHelpCommand(self):
            helpText = self.Help if hasattr(self, "Help") else ""
            self.context.Logger.INFO('\t\t'.join(('\t\t' + helpText.lstrip()).splitlines(True)))

