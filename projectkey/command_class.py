import os, inspect, sys

class CommandClass(object):
    def __init__(self, projectkey_class):
        self.projectkey_class = projectkey_class
        self.projectkey_file = inspect.getfile(self.projectkey_class)

        self.commands = {}
        for method_name, actual_method in inspect.getmembers(self.projectkey_class, inspect.ismethod):
            if not method_name.startswith("_") and inspect.getmodule(actual_method).__name__ != 'projectkey.keyclass':
                docstring = "" if actual_method.__doc__ is None else actual_method.__doc__
                argspec = inspect.getargspec(actual_method)
                args = argspec.args[1:]
                varargs = argspec.varargs
                keyargs = argspec.keywords
                defaults = argspec.defaults

                if varargs is not None and keyargs is not None:
                    print "Method '%s' in key.py cannot have both *args and **kwargs" % method_name
                    sys.exit(1)

                minargs = maxargs = 0
                if varargs is not None or keyargs is not None:
                    maxargs = 255
                    minargs = len(args)
                    argdocs = ['[%s1]' % varargs[:-1], '[%s2]' % varargs[:-1], '[%s3]' % varargs[:-1], '...',]
                else:
                    maxargs = len(args)
                    if defaults is not None:
                        minargs = len(args) - len(defaults)
                        argdocs = ['%s' % x for x in args[:minargs]] + ['[%s]' % x for x in args[minargs:]]
                    else:
                        minargs = len(args)
                        argdocs = ['%s' % x for x in args]
                
                self.commands[method_name] = {
                    'helptext': docstring,
                    'onelinehelp': docstring.split('\n')[0],
                    'function': actual_method,
                    'linenumber': inspect.findsource(actual_method)[1],
                    'minargs': minargs,
                    'maxargs': maxargs,
                    'argdocs': argdocs,
                    'args': args,
                    'varargs': varargs,
                    'keywords': keyargs,
                    'defaults': inspect.getargspec(actual_method).defaults,
                }

    def correct_args(self, command, number):
        return self.commands[command]['minargs'] <= number and self.commands[command]['maxargs'] >= number

    def arg_help(self, command):
        return ' '.join(self.commands[command]['argdocs'])

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
            print "Command '%s' not found in %s. Type 'd help' to see a full list of commands." % (command, self.projectkey_file)

    def print_help(self):
        print "Usage: k command [args]\n"
        if self.projectkey_class.__doc__ is not None:
            print "%s\n" % self.projectkey_class.__doc__
        length_of_longest_command = self.length_of_longest_command()

        for name, command in self.sorted_commands():
            if command['helptext']:
                print "  %s - %s" % (name.rjust(length_of_longest_command), command['onelinehelp'])

        print
        print "Run 'd help [command]' to get help on a particular command."

    def run_command(self, command, command_args):
        """Run a ProjectKey command with a list of command_args."""
        if command in self.command_list():
            if self.commands[command]['minargs'] <= len(command_args) <= self.commands[command]['maxargs']:
                # Feed it the relevant directories
                self.projectkey_class.KEYDIR = os.path.abspath(os.path.dirname(self.projectkey_file))
                self.projectkey_class.CWD = os.getcwd()

                # Initialize class and run
                projectkey_obj = self.projectkey_class()
                returnvalue = getattr(projectkey_obj, command)(*command_args)
                
                # If command returns something, print it
                if returnvalue is not None and returnvalue != 0:
                    print returnvalue
            else:
                print "Incorrect number of arguments for command '%s'.\n" % command
                print "Arguments used: \"%s\"" % '\"'.join(command_args)
                self.help_command(command)
                return 1
        else:
            print "Command '%s' not found in %s" % (command, self.projectkey_file)
            return 1