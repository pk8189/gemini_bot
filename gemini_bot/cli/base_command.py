from argparse import Namespace
from os import environ

from gemini_bot.clients import PublicClient, PrivateClient

class BaseCommand(PublicClient, PrivateClient):
    def __init__(self, sandbox=True):
        if "public" in self.__module__:
            self.client = PublicClient()
        else:
            self.client = PrivateClient(sandbox=sandbox)

    def run(self, args: Namespace):
        output = self.handle(args)
        return output

    def handle(self, args: Namespace):
        """Starting point of the actual logic of the command"""
        raise NotImplementedError
