# -*- coding: utf-8 -*-
import os
import sys
from fabric.api import run
from fabric.api import task
from fabric.api import local


def check_virtualenv():
    if not os.path.exists('virtenv'):
        print(' !! I need a virtualenv (virtenv). Run "fab init_virtualenv".')
        sys.exit(1)


@task
def update_requirements(env="dev"):
    check_virtualenv()
    local('virtenv/bin/pip install -r requirements/%s.txt' % env)


@task
def runserver():
    check_virtualenv()
    local('virtenv/bin/python manage.py runserver')


@task
def syncdb():
    check_virtualenv()
    local('virtenv/bin/python manage.py syncdb')
    local('virtenv/bin/python manage.py migrate')


@task
def collectstatic():
    check_virtualenv()
    local('virtenv/bin/python manage.py collectstatic')


def virtualenv(command):
    local('source virtenv/bin/activate && ' + command)


@task
def init_virtualenv():
    local('virtualenv virtenv')


@task
def update_messages():
    local('virtenv/bin/python manage.py makemessages -l fr -i virtenv -i venv')


@task
def compile_messages():
    local('virtenv/bin/python manage.py compilemessages')


@task
def deploy():
    run('cd /var/www/www.mylenela.fr && git pull')
    run('cd /var/www/www.mylenela.fr && virtenv/bin/pip install -r requirements.txt')
    run('cd /var/www/www.mylenela.fr && virtenv/bin/python manage.py syncdb')
    run('cd /var/www/www.mylenela.fr && virtenv/bin/python manage.py migrate')
    run('cd /var/www/www.mylenela.fr && virtenv/bin/python manage.py collectstatic --noinput')
    run('cd /var/www/www.mylenela.fr && virtenv/bin/python manage.py mtime_cache --clean')
    run('cd /var/www/www.mylenela.fr && virtenv/bin/python manage.py compress')
