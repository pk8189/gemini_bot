from argparse import ArgumentParser, Namespace
from typing import Any, Callable
from pathlib import Path
import inspect

from dotenv import load_dotenv

from gemini_bot.cli.base_command import BaseCommand
from gemini_bot.cli.commands import public, private

def main() -> None:
    env_path = Path.cwd() / ".env"
    load_dotenv(dotenv_path=env_path)
    public_commands = [C for (name, C) in inspect.getmembers(public, inspect.isclass) if C.__bases__[0] == BaseCommand]
    private_commands = [C for (name, C) in inspect.getmembers(private, inspect.isclass) if C.__bases__[0] == BaseCommand]
    commands = public_commands + private_commands
    parser = create_parser(commands)
    instantiated_commands = [C() for C in commands]
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
        try:
            subcommand().add_arguments(subparser)
        except:
            # no add_arguments function supplied to parser
            pass
    return parser
