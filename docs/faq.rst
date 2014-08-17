FAQ
===

* Why is the script called 'd'?

Because you will probably be running it a lot. One letter command means fewer
keystrokes to wear you and your keyboard out.

Apologies if you already have a command called d!

* Won't the dev.py file size grow and spiral out of control? Maybe one script per command is better?

It might grow, but that's usually a sign that you should break out some of the tasks into separate files.
I find that the number of commands stabilizes at around 12-13 and don't usually grow more than 5 lines long each.

Sometimes it might make sense to create new dev.py files in separate directories (e.g. a production environment directory)
so that in separate contexts you can run different commands. All of this is up to you, of course.

* Is this just for python projects?

No, you can use it in any environment.

* Why not just use a shell script?

I actually used to just use it as a shell script, but the shell script spiralled out of control as I added features.

In python you can get the best of both worlds as shown above, especially if you use amoffat's wonderful sh.

* Should I install DevKey in a virtualenv?

You can, but unless you activate it the 'd' command won't be accessible from everywhere.

I recommend installing it outside a virtualenv even if you're going to be using a project that has a virtualenv.

* This is neat!

Thanks. If you'd like to repay me, drop me an email and let me know where you're using it.
