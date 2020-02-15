from argparse import ArgumentParser, Namespace

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
