from argparse import ArgumentParser, Namespace
from os import getenv

from gemini_bot.clients import GeminiPrivateClient
from gemini_bot.cli.base_command import BaseCommand

class GetBalance(BaseCommand):

    name = "get_balance"

    def handle(self, args: Namespace):
        print(self.client.get_balance())

    def add_arguments(self, parser: ArgumentParser) -> None:
        pass

class NewOrder(BaseCommand):

    name = "new_order"

    def handle(self, args: Namespace):
        print(
            self.client.new_order(
                args.symbol,
                args.amount,
                args.price,
                args.side
            )
        )

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-s", "--symbol", required=True, help="Symbol to buy"
        )
        parser.add_argument(
            "-a", "--amount", required=True, help="Amount to buy"
        )
        parser.add_argument(
            "-p", "--price", required=True, help="Price to buy at"
        )
        parser.add_argument(
            "--side", required=True, help="Buy or sell"
        )

class Status(BaseCommand):

    name = "status"

    def handle(self, args: Namespace):
        missing_env_vars = self.what_is_missing_for_login()
        if missing_env_vars:
            for missing_env_var in missing_env_vars:
                print(f"Please set {missing_env_var} to login.")
        elif not GeminiPrivateClient().private_client:
            print("Unable to authenticate with the given API keys")
        else:
            print("You are logged in!")

    def what_is_missing_for_login(self):
        needed_keys = ["API_KEY", "API_SECRET"]
        return [needed_key for needed_key in needed_keys if not getenv(needed_key, False)]
