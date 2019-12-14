from argparse import Namespace

from gemini_bot.clients import PublicClient, PrivateClient

class BaseCommand():

    def run(self, args: Namespace):
        if "cli.commands.public" in self.__module__:
            self.client = PublicClient()
        if "cli.commands.private" in self.__module__:
            self.client = PrivateClient()
        output = self.handle(args)
        return output

    def handle(self, args: Namespace):
        """Entry point"""
        raise NotImplementedError
