Why?
====

Every project I've ever worked upon has had a multitude of scripts,
long, repetitive one liners to do all of the following and more:

* Set up environments
* Run development services - web server, mock SMTP server, task queue, etc.
* Run various lint tools
* Run tests.
* Dump/load data from the database.
* Tail logs on production.
* ssh into production servers.
* Run deployment scripts.
* Perform common commit/merging/rebase workflows.
* Common interaction tasks with docker/vagrant/ansible/puppet/etc.

These scripts were often non-existent (cue furious tapping for all of
the long one liners), spread all over the repo in hard to find places
or even buried in wiki pages that were describing scripts that *should*
exist but don't.

dev.py provides a way to centralize these into one self-documenting file
at the root of your repo that can be called from anywhere.
