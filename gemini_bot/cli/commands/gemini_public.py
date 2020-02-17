from argparse import ArgumentParser, Namespace

from gemini_bot.cli.base_command import BaseCommand
from gemini_bot.terminal_colors import success, warning, message

class Symbols(BaseCommand):

    name = "symbols"

    def handle(self, args: Namespace):
        print(self.client.symbols())

    def add_arguments(self, parser: ArgumentParser) -> None:
        pass

class GetLast500Trades(BaseCommand):

    name = "get_last_500_trades"

    def handle(self, args: Namespace):
        print(self.client.get_last_500_trade_history(args.symbol))

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-s", "--symbol", required=True, help="Symbol to query"
        )

class GetTicker(BaseCommand):

    name = "get_ticker"

    def handle(self, args: Namespace):
        print(self.client.get_ticker(args.symbol))

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-s", "--symbol", required=True, help="Symbol to query"
        )

class GetCurrentOrderBook(BaseCommand):

    name = "get_current_order_book"

    def handle(self, args: Namespace):
        res = self.client.get_current_order_book(args.symbol)
        print(message("Bids:"))
        print(success(res["bids"]))
        print(message("Asks"))
        print(warning(res["asks"]))

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-s", "--symbol", required=True, help="Symbol to query"
        )

class GetAuctionHistory(BaseCommand):

    name = "get_auction_history"

    def handle(self, args: Namespace):
        print(self.client.get_auction_history(args.symbol, args.since))

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-s", "--symbol", required=True, help="Symbol to query"
        )
        parser.add_argument(
            "-d", "--since", help="Date to get trade history since"
        )
