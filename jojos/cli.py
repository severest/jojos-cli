"""
jojos

Usage:
  jojos hello
  jojos -h | --help
  jojos --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  jojos hello

Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/severest/jojos-cli
"""


from inspect import getmembers, isclass

from docopt import docopt

from . import __version__ as VERSION


def main():
    """Main CLI entrypoint."""
    import jojos.commands
    options = docopt(__doc__, version=VERSION)

    # Here we'll try to dynamically match the command the user is trying to run
    # with a pre-defined command class we've already created.
    for (k, v) in options.items():
        if hasattr(jojos.commands, k) and v:
            module = getattr(jojos.commands, k)
            jojos.commands = getmembers(module, isclass)
            command = [command[1] for command in jojos.commands if command[0] != 'Base'][0]
            command = command(options)
            command.run()
