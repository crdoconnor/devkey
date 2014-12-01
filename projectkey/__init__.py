#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

# The version as used in the setup.py and the docs conf.py
__version__ = "0.1"


class ProjectKey(object):
    """Base ProjectKey class."""
    pass

import k_runner
import interpreter
import os

cli = interpreter.cli_interface
cd = os.chdir

def run(shell_commands, get_output=False):
    """Run shell commands."""
    import subprocess
    for shell_command in shell_commands.split('\n'):
        if get_output:
            return subprocess.check_output(shell_command, shell=True)
        else:
            subprocess.check_call(shell_command, shell=True)

