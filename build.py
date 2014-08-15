print "Building..."

from fabric.api import env
from fabric.operations import run, put, sudo
from fabric.tasks import execute


env.hosts = ['mbjerkness@bjerkness.net']
env.key_filename = "id_rsa"

def copy():
    # make sure the directory is there!
    sudo('mkdir -p /opt/local/mongo')
    sudo('chown mbjerkness /opt/local/mongo')
    # our local 'testdirectory' - it may contain files or subdirectories ...
    put('index.html', '/opt/local/mongo/')
    put('assets', '/opt/local/mongo/')
    put('images', '/opt/local/mongo/')

results = execute(copy)
