#!/usr/bin/python
# PYTHON_ARGCOMPLETE_OK
import sys
import os
import imp

def run():
    base = os.path.dirname(os.path.dirname(os.path.abspath(os.path.realpath(__file__))))
    sys.path.insert(0, base)
    from devkey import interpreter
    return interpreter.interpreter()


if __name__ == '__main__':
    exit = run()
    if exit:
        sys.exit(exit)
