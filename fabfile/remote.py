# -*- coding: utf-8 -*-
from fabric.api import env, sudo, task, cd, run, prefix
from contextlib import contextmanager

import config

__all__ = ['restart', 'deploy','update', 'git_pull', 'git_reset', 'test']

@contextmanager
def virtualenv():
    with cd(env.project_path):
        with prefix('source %s/bin/activate' % env.virtualenv):
            yield

@task
def restart():
    """ Restart web server """
    with virtualenv():
        run(env.restart_web_server_command)

@task
def test():
    """ Run unit tests on host """
    with virtualenv():
        run('python manage.py test')

@task
def git_pull():
    """ Downloads and marge data from remote repository."""
    with virtualenv():
        run('git pull %(parent)s %(branch)s' % env)

@task
def git_reset(hash):
    """
    Performs a hard reset repository

    $fab remote.git_reset:hash="hash"
    """
    with virtualenv():
        run("git reset --hard $(hash)")

def _build(run_local_deployment=True):
    with virtualenv():
        if run_local_deployment:
            run('fab local_tasks.deploy')
        run('python manage.py syncdb')
        run('python manage.py migrate')

@task
def deploy():
    git_pull()
    _build()
    test()
    restart()

@task
def update():
    """
    Updatne code and restarts the server.
    """
    git_pull()
    _build(False)
    restart()
