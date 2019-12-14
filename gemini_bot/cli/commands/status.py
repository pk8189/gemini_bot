from argparse import ArgumentParser, Namespace
from pathlib import Path
from os import getenv
import dotenv

from gemini_bot.cli.base_command import BaseCommand
from gemini_bot.clients import PrivateClient

class Status(BaseCommand):

    name = "status"

    def handle(self, args: Namespace):
        missing_env_vars = self.what_is_missing_for_login()
        if missing_env_vars:
            for missing_env_var in missing_env_vars:
                print(f"Please set {missing_env_var} to login.")
        elif not PrivateClient().private_client:
            print("Unable to authenticate with the given API keys")
        else:
            print("You are logged in!")
        production_mode = getenv("PRODUCTION_MODE") == "True"
        if production_mode:
            print("You are in production mode. Unset PRODUCTION_MODE=True to switch to sandbox mode")
        else:
            print("You are in sandbox mode")


    def add_arguments(self, parser: ArgumentParser) -> None:
        pass


    def what_is_missing_for_login(self):
        needed_keys = ["API_KEY", "API_SECRET"]
        return [needed_key for needed_key in needed_keys if not getenv(needed_key, False)]