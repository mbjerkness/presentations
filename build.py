print "Building..."

from fabric.api import env
from fabric.operations import run, put, sudo
from fabric.tasks import execute


env.hosts = ['mbjerkness@bjerkness.net']
env.key_filename = "id_rsa"

def copy():
    # make sure the directory is there!
    sudo('mkdir -p /opt/local/mongo_aws')
    sudo('chown mbjerkness /opt/local/mongo_aws')
    
    # our local 'testdirectory' - it may contain files or subdirectories ...
    put('index.html', '/opt/local/mongo_aws/')
    put('assets', '/opt/local/mongo_aws/')
    put('images', '/opt/local/mongo_aws/')

results = execute(copy)
