# -*- coding: utf-8 -*-
from fabric.api import task, env

import remote
import local_tasks

import config

@task(alias='local')
def localenv():
    """
    Set the configuration for localhost
    """
    import config
    env.hosts = ['localhost']
    env.parent = config.PARENT
    env.branch = config.BRANCH
    env.project_path = config.PROJECT_PATH
    env.restart_web_server_command = config.RESTART_WEB_SERVER_COMMAND
    env.virtualenv = config.PATH
