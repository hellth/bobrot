# -*- coding: utf-8 -*-
import os
from fabric.api import task, local
from fabric.colors import green

__all__ = [
    'prepare_folders', 'prepare_static', 'build',
    'install_dependencies'
]

PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(
    os.path.join(PATH,  '..', 'invoices'))
PROJECT_ROOT = os.path.dirname(os.path.join(PATH,  '..' , '..'))

@task
def prepare_folders():
    path_list = [
        [PROJECT_PATH, 'static'],
        [PROJECT_PATH, 'templates'],
    ]
    for paths in path_list:
        path = os.path.join(*paths)
        if not os.path.exists(path):
            os.mkdir(path, 0755)
            print '%s %s' % (green('Create:'), path)

@task
def prepare_static():
    local('python manage.py collectstatic')

@task
def install_dependencies():
    local(
        'pip install -r %s/requirements_apps.txt' % PROJECT_ROOT)

@task
def build():
    prepare_folders()
    prepare_static()
    install_dependencies()
