Quickstart
==========

Step 1: Put this file into the root of your project and call it dev.py:

'''
"""Yourproject development environment commands."""
from os import system as s, chdir as cd
from sh import hg
import os

def runserver():
    """Run django debug web server on port 8000"""
    cd(DEVDIR)
    s("./venv/bin/python manage.py runserver 8000 --traceback --settings=yourproject.local_settings")

def upgrade():
    """pip upgrade on all packages and freeze afterwards."""
    cd(DEVDIR)
    s("./venv/bin/pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs ./venv/bin/pip install -U")
    s("./venv/bin/pip freeze > ./requirements.txt")

def smtp():
    """Run smtp server on port 25025."""
    print "Running SMTP server..."
    s("python -m smtpd -n -c DebuggingServer localhost:25025")

def s()
    """Run hg status."""
    s("hg status")

def striptrailingwhitespace():
    """strip the trailing whitespace from all files in repo."""
    cd(DEVDIR)
    repofiles = hg("locate", "*.py").split('\n')
    repofiles.remove('')
    for filename in repofiles:
        with open(filename, 'r') as fh:
            new = [line.rstrip() for line in fh]
        with open(filename, 'w') as fh:
            [fh.write('%s\n' % line) for line in new]
'''

Step 2: Run: sudo pip install devkey sh

Step 3: Run: "sudo activate-global-python-argcomplete" (optional; this will give you autocomplete)

Step 3: Run the 'd' command in any folder in your project:

'''
$ d help
Usage: d command [args]

Yourproject development environment commands.

                runserver - Run django debug web server on port 8000
                  upgrade - pip upgrade on all packages and freeze afterwards.
                     smtp - Run smtp server on port 25025.
                        s - Run hg status.
  striptrailingwhitespace - strip the trailing whitespace from all files in mercurial repo.

Run 'd help [command]' to get help on a particular command.

'''

Step 4: Add more commands!
