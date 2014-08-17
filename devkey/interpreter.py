import os, sys, command_module
import argcomplete, argparse

def check_directories():
    """Check every directory from the current all the way to / for a file named dev.py."""
    checkdirectory = os.getcwd()
    directories_checked = []
    devpy_filename = None
    while checkdirectory != '/':
        directories_checked.append(checkdirectory)
        if os.path.exists("%s/dev.py" % checkdirectory):
            devpy_filename = "%s/dev.py" % checkdirectory
            break
        else:
            checkdirectory = os.path.abspath(os.path.join(checkdirectory, os.pardir))
    return (devpy_filename, directories_checked)

def interpreter():
    args = sys.argv
    devpy_filename, directories_checked = check_directories()

    if not devpy_filename:
        print "dev.py not found in the following directories:\n"
        print '\n'.join(directories_checked)
        print "\nSee http://github.io/crdoconnor/devkey"
        return 1
    else:
        cm = command_module.CommandModule(devpy_filename)
        parser = argparse.ArgumentParser(add_help=False)
        parser.add_argument("commands", nargs='*', default=None).completer = cm.command_completer
        argcomplete.autocomplete(parser)
        parsed_args = parser.parse_args()
        commands = parsed_args.commands

        if len(commands) == 0:
            cm.print_help()
        elif len(commands) == 2 and commands[0] in ['-h', '--help', 'help']:
            cm.help_command(commands[1])
        else:
            cm.run_command(commands[0], commands[1:])
        return 0
