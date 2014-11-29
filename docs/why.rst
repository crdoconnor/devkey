Why?
====

* Why do I need ProjectKey? I already have ant/fabric/nose/salt/ansible/docker

ProjectKey is not a tool intended to replace these tools, it is a tool that is
intended to *invoke* these tools.

You could write a whole build script in a key.py command, but using other,
more specific tools is generally advisable.

Every project I've ever worked upon has nonetheless had a multitude of scripts,
long, repetitive one liners to do all of the following and more:

* Set up environments
* Run development services - web server, mock SMTP server, task queue, etc.
* Run various lint tools
* Run tests
* Create builds
* Create skeleton code.
* Dump/load data from the database.
* Upgrade dependencies
* Tail logs on production.
* ssh into production servers.
* Run deployment scripts.
* Perform common commit/merging/rebase workflows.
* Common interaction tasks with docker/vagrant/ansible/puppet/etc.

It is intended to cut down these types of unnecessary interactions:

"Hey buddy, can you Skype me the command to run lint using our config file?"

"How do you run a test again?"

"What's the exact command to run a development web server? I tried but it isn't working for me."

The scripts to do these things are often non-existent spread all over the repo in hard to find places:

"You mean we actually do have a script to deploy docker?"

or even buried in wiki pages that were describing scripts that should
exist but don't.

STEPS TO CREATE A NEW BUILD AND DEPLOY IT

ProjectKey provides a way to centralize these into one self-documenting file
at the root of your repo that can be called from anywhere.
