ProjectKey
==========

Three step process to create your personlized suite of custom project commands that you can invoke with one key:

Step 1: Run: "sudo pip install projectkey ; sudo activate-global-python-argcomplete"

Step 2: Create a key.py file at the top folder of your project like this::
    
    from projectkey import ProjectKey, cli, cd, run

    class YourDjangoProjectKey(ProjectKey):
        """Yourproject development environment commands."""
        PROJECTNAME = "yourproject"
        
        def runserver(self):
            """Run django debug web server on port 8080."""
            print "Running webserver..."
            cd(self.KEYDIR)
            run("./venv/bin/python manage.py runserver_plus 8080 --traceback --settings=%s.dev_settings" % self.PROJECTNAME)

        def upgrade(self):
            """pip upgrade on all packages and freeze afterwards."""
            cd(self.KEYDIR)
            run("""
                ./venv/bin/pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs ./venv/bin/pip install -U
                ./venv/bin/pip freeze > ./requirements.txt
            """)

        def smtp(self):
            """Run smtp server on port 25025."""
            print "Running SMTP server..."
            run("python -m smtpd -n -c DebuggingServer localhost:25025")
        
        def striptrailingwhitespace(self):
            """strip the trailing whitespace from all files in repo."""
            cd(self.KEYDIR)
            repofiles = run_return("hg locate *.py").split('\n')
            repofiles.remove('')
            for filename in repofiles:
                with open(filename, 'r') as fh:
                    new = [line.rstrip() for line in fh]
                with open(filename, 'w') as fh:
                    [fh.write('%s\n' % line) for line in new]

        def inspectfile(self, *filenames):
            """Inspect file(s) for pylint violations."""
            cd(self.CWD)
            run("{0}/venv/bin/pylint --rcfile={0}/pylintrc -r n {1}".format(self.KEYDIR, ' '.join(filenames)))

Step 3: Run the 'k' command in any folder below your project::

    $ k help
    Usage: k command [args]
    
    Yourproject development environment commands.
    
                    runserver - Run django debug web server on port 8000
                      upgrade - pip upgrade on all packages and freeze afterwards.
                         smtp - Run smtp server on port 25025.
      striptrailingwhitespace - strip the trailing whitespace from all files in mercurial repo.
                  inspectfile - Inspect file(s) for pylint violations.
    
    Run 'd help [command]' to get more help on a particular command.

Step 4: Add more commands!


Features
========

* Autodocuments using your docstrings.
* Use variables self.KEYDIR or self.CWD in any command to refer to ProjectKey's directory or the directory you ran k in.
* Passes any arguments on to the method via the command line.
* Autocomplete works out of the box.
* Comes with shortcut command to run lists of shell commands directly, so you can copy and paste directly from existing bash scripts.
* Use the full power of python to enhance your team's development environment and automate all of the things.

For more documentation, see https://projectkey.readthedocs.org/
