#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

import os, sys, imp, inspect, command_class
import argcomplete, argparse

def interpreter():
    """CLI interpreter for the k command."""
    # Check every directory from the current all the way to / for a file named key.py
    checkdirectory = os.getcwd()
    directories_checked = []
    keypy_filename = None
    while checkdirectory != '/':
        directories_checked.append(checkdirectory)
        if os.path.exists("%s/key.py" % checkdirectory):
            keypy_filename = "%s/key.py" % checkdirectory
            break
        else:
            checkdirectory = os.path.abspath(os.path.join(checkdirectory, os.pardir))

    if not keypy_filename:
        print "key.py not found in the following directories:\n"
        print '\n'.join(directories_checked)
        print "\nSee http://keycom.readthedocs.org/en/latest/quickstart.html"
        return 1
    else:
        # All classes in key.py
        pyclasses = inspect.getmembers(imp.load_source("key", keypy_filename), inspect.isclass)
        
        if "KeyCom" not in [pyclass[0] for pyclass in pyclasses]:
            print "KeyCom class not found in key.py."
            print "\nSee http://keycom.readthedocs.org/en/latest/quickstart.html"
            return 1

        keycom_class = [pyclass[1] for pyclass in pyclasses if pyclass[0] == "KeyCom"][0]
#        import IPython
#        IPython.embed()
        cli_interface(keycom_class)

def cli_interface(keycom_class):
    """CLI interpreter for the KeyCom class itself."""
    cc = command_class.CommandClass(keycom_class)
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("commands", nargs='*', default=None).completer = cc.command_completer
    argcomplete.autocomplete(parser)
    commands = parser.parse_args().commands

    if len(commands) == 0 or len(commands) == 1 and commands[0] in ['-h', '--help', 'help']:
        cc.print_help()
    elif len(commands) > 1 and commands[0] in ['-h', '--help', 'help']:
        cc.help_command(commands[1])
    else:
        cc.run_command(commands[0], commands[1:])
    return 0
