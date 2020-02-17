from argparse import Namespace

from gemini_bot.clients import (
    GeminiPublicClient,
    GeminiPrivateClient,
    CryptoDataDownloadClient,
)

class BaseCommand():

    def run(self, args: Namespace):
        if "cli.commands.gemini_public" in self.__module__:
            self.client = GeminiPublicClient()
        if "cli.commands.gemini_private" in self.__module__:
            self.client = GeminiPrivateClient()
        if "cli.commands.crypto_data_download" in self.__module__:
            self.client = CryptoDataDownloadClient()
        # pylint: disable=maybe-no-member
        output = self.handle(args)
        return output
