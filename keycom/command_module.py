import os, imp, inspect
from argcomplete import warn

class CommandModule(object):
    def __init__(self, devpy_filename):
        self.devpy_filename = devpy_filename
        self.dev_module = imp.load_source("dev", devpy_filename)

        self.commands = {}
        for method_name, actual_method in inspect.getmembers(self.dev_module, inspect.isfunction):
            if not method_name.startswith("_"):
                docstring = "" if actual_method.__doc__ is None else actual_method.__doc__
                self.commands[method_name] = {
                    'helptext': docstring,
                    'onelinehelp': docstring.split('\n')[0],
                    'function': actual_method,
                    'linenumber': inspect.findsource(actual_method)[1],
                    'args': inspect.getargspec(actual_method).args,
                    'varargs': inspect.getargspec(actual_method).varargs,
                    'keywords': inspect.getargspec(actual_method).keywords,
                    'defaults': inspect.getargspec(actual_method).defaults,
                }

    def correct_args(self, command, number):
        if self.commands[command]['varargs'] is not None:
            return True
        elif len(self.commands[command]['args']) == number:
            return True
        else:
            return False

    def arg_help(self, command):
        if self.commands[command]['varargs'] is not None:
            vararg_name = self.commands[command]['varargs']
            if vararg_name[-1] == "s":
                vararg_name = vararg_name[:-1]
            return "[%s1] [%s2] [%s3] ..." % (vararg_name, vararg_name, vararg_name)
        elif len(self.commands[command]['args']) > 0:
            return ' '.join([arg for arg in self.commands[command]['args']])
        else:
            return ""

    def command_list(self):
        return self.commands.keys()

    def command_completer(self, prefix, parsed_args, **kwargs):
        existing_commands = parsed_args.commands
        if len(existing_commands) == 0:
            return (v for v in self.command_list() + ['help'] if v.startswith(prefix)) 
        else:
            if existing_commands[0] in ["help", "--help", "-h"]:
                return (v for v in self.command_list() + ['help'] if v.startswith(prefix))

    def sorted_commands(self):
        return sorted(self.commands.items(), key=lambda command: command[1]['linenumber'])

    def length_of_longest_command(self):
        return sorted([len(name) for name, _ in list(self.commands.items())], reverse=True)[0]
    
    def help_command(self, command):
        if command in self.command_list():
            print "Usage: d %s %s" % (command, self.arg_help(command))
            print
            print self.commands[command]['helptext']
        else:
            print "Command '%s' not found in %s. Type 'd help' to see a full list of commands." % (command, self.devpy_filename)

    def print_help(self):
        print "Usage: d command [args]"
        print
        print self.dev_module.__doc__
        print
        length_of_longest_command = self.length_of_longest_command()

        for name, command in self.sorted_commands():
            if command['helptext']:
                print "  %s - %s" % (name.rjust(length_of_longest_command), command['onelinehelp'])

        print
        print "Run 'd help [command]' to get help on a particular command."

    def run_command(self, command, dev_command_args):
        if command in self.command_list():
            if self.correct_args(command, len(dev_command_args)):
                getattr(self.dev_module, command).func_globals['DEVDIR'] = os.path.abspath(os.path.dirname(self.devpy_filename))
                getattr(self.dev_module, command).func_globals['CWD'] = os.getcwd()
                getattr(self.dev_module, command)(*dev_command_args)
            else:
                print "Incorrect number of arguments for command '%s'.\n" % command
                self.help_command(command)
        else:
            print "Command '%s' not found in %s" % (command, self.devpy_filename)
