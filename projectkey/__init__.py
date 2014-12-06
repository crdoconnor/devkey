#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK

from __future__ import print_function

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

def run(shell_commands, ignore_errors=True):
    """Run shell commands."""
    import subprocess
    try:
        import subprocess
        for shell_command in shell_commands.split('\n'):
            subprocess.check_call(shell_command, shell=True)
    except subprocess.CalledProcessError, error:
        if error.output is not None:
            print(error.output)
        if not ignore_errors:
            sys.exit(1)

def run_return(shell_command):
    """Run shell commands and return the output."""
    import subprocess
    return subprocess.check_output(shell_command, shell=True)
