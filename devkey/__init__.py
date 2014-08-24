#!/usr/bin/env python
import interpreter

# The version as used in the setup.py and the docs conf.py
__version__ = "0.1.1"

if __name__ == '__main__':
    exit = interpreter.interpreter()
    if exit:
        sys.exit(exit)
