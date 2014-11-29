FAQ
===


* Why is the script called 'k' and not 'projectkey'?

Because you will probably be running it a lot. A one letter command means fewer
keystrokes to wear you and your keyboard out.

* Won't the key.py file size grow and spiral out of control? Maybe one script per command is better?

It might grow uncontrollably, but that's usually a sign that you should break out some of the tasks into separate files, modules, scripts and even projects.

* Is this just for python projects?

No, you can use it on any project, you just have to create the commands in python (or just translate shell commands).

* I already have a bunch of shell scripts. What does this give me?

1) All of your project commands get united under one easy to use, discoverable, self documenting file that you can call up with one key.
2) It can be run even if you are inside your project's directory and six levels deep.
3) You can translate almost any line in your bash script to use this self.sc("your command here") so it's not hard to switch.
4) You can use a programming language that doesn't suck.

* self.sc("") is bad because it invokes the shell. Haven't you heard of shellshock? Why does it do this?!

A) Invoking the shell is only a security issue if you are using untrusted input. Everybody who uses a ProjectKey ought to be trusted. That's why they're running it *from* a shell.

B) The reason I do it is that makes it easier to transpose existing shell scripts line by line into the ProjectKey without translating them into python. E.g. this:

"""./venv/bin/pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs ./venv/bin/pip install -U"""

It's ugly. It's non pythonic. But goddamn it, it works so I'm not rewriting it.

* Should I install DevKey in a virtualenv?

You can, and it will work, but if you do that you won't be able to use the k command unless the virtual environment is active.

If you don't have root, this might be the only way of installing it, however.

* This is neat!

Thanks. If you'd like to repay me, drop me an email and let me know where you're using it.
