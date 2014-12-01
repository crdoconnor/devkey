import os, sys, command_class
import argcomplete, argparse

def cli_interface(projectkey_class):
    """CLI interpreter for the ProjectKey class itself."""
    cc = command_class.CommandClass(projectkey_class)
    parser = argparse.ArgumentParser(add_help=False, prefix_chars=[None,])
    parser.add_argument("commands", nargs='*', default=None).completer = cc.command_completer
    argcomplete.autocomplete(parser)
    commands = parser.parse_args().commands

    if len(commands) == 0 or len(commands) == 1 and commands[0] in ['-h', '--help', 'help']:
        returnval = cc.print_help()
    elif len(commands) > 1 and commands[0] in ['-h', '--help', 'help']:
        returnval = cc.help_command(commands[1])
    else:
        returnval = cc.run_command(commands[0], commands[1:])
    sys.exit(returnval)
