from argparse import ArgumentParser, Namespace

from gemini_bot.cli.base_command import BaseCommand

class GetBalance(BaseCommand):

    name = "get_balance"

    def handle(self, args: Namespace):
        print(self.client.get_balance())

    def add_arguments(self, parser: ArgumentParser) -> None:
        pass