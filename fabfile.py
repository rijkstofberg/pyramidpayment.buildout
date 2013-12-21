"""
Deploy
------

.. sourcecode:: bash

    $ python2.6 bootstrap.py -c development.cfg
    $ bin/buildout -c development.cfg
    $ bin/fab --list
    $ bin/fab deploy


Available Fabric commands
-------------------------
"""

from fabric.api import env
from niteoweb.fabfile.project import *

import os

env.path = os.getcwd()
env.hosts = ['SERVER_IP']
env.prod_user = 'pyramid.payment'  # production user for this project
env.server = 'SERVER_IP'
env.shortname = 'pyramid.payment'


def deploy():
    """A high-level meta-command for deploying this project to Omega
    server."""

    configure_nginx()
    download_code()
    prepare_buildout()
    run_buildout()
    start_supervisord()
