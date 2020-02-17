from argparse import ArgumentParser, Namespace

from gemini_bot.cli.base_command import BaseCommand

class DownloadData(BaseCommand):

    name = "download_data"

    def __init__(self):
        self.symbols = [
            "btcusd",
            "ethusd",
            "ltcusd",
            "zecusd",
            "zecbtc",
            "zeceth",
        ]
        self.frequency_mapper = {
            "daily": "d",
            "hourly": "1hr",
            "minute" : "2019_1min",
        }

    def handle(self, args: Namespace):
        try:
            frequency = self.frequency_mapper[args.frequency]
        except ValueError:
            raise (f"Invalid freqency choice. Choose from {self.frequency_mapper.keys()}")
        pickle_saved_name = self.client.get_and_save_data(args.symbol, frequency)
        print(f"Saved csv as dataframe in pickle file {pickle_saved_name}")

    def add_arguments(self, parser: ArgumentParser) -> None:
        parser.add_argument(
            "-s", "--symbol", required=True, help="Symbol to query", choices=self.symbols,
        )
        parser.add_argument(
            "-f",
            "--frequency",
            help="Frequency",
            choices=list(self.frequency_mapper.keys()),
            default="daily",
        )
