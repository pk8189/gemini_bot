from argparse import Namespace

from gemini_bot.clients import GeminiPublicClient, GeminiPrivateClient

class BaseCommand():

    def run(self, args: Namespace):
        if "cli.commands.public" in self.__module__:
            self.client = GeminiPublicClient()
        if "cli.commands.private" in self.__module__:
            self.client = GeminiPrivateClient()
        # pylint: disable=maybe-no-member
        output = self.handle(args)
        return output
