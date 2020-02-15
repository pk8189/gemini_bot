from argparse import ArgumentParser, Namespace
from typing import Any, Callable
from pathlib import Path

from dotenv import load_dotenv

from gemini_bot.cli.commands import commands

def main() -> None:
    env_path = Path.cwd() / ".env"
    load_dotenv(dotenv_path=env_path)
    instantiated_commands = [C() for C in commands]
    parser = create_parser(commands)
    args, _ = parser.parse_known_args()
    cs = {command.name: command for command in instantiated_commands}
    command = cs.get(args.command, None)
    if not command:
        return parser.print_help()
    run(command, args)

def run(command: Any, args: Namespace) -> Callable:
    try:
        return command.run(args)
    except SystemError as e:
        print(e)

def create_parser(subcommands: list) -> ArgumentParser:
    """Adds predict arguments to parser.

    :return: Namespace arguments
    """
    parser = ArgumentParser(prog="gemini_bot")
    subparsers = parser.add_subparsers(dest="command")
    for subcommand in subcommands:
        subparser = subparsers.add_parser(subcommand.name)
        subcommand().add_arguments(subparser)
    return parser
