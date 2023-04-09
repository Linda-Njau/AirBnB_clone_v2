#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""

from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = '<username>'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if not exists(archive_path):
        return False

    file_name = archive_path.split('/')[-1]
    folder_name = file_name.split('.')[0]
    releases_path = "/data/web_static/releases"
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("sudo mkdir -p {}/{}/".format(releases_path, folder_name))
        run("sudo tar -xzf /tmp/{} -C {}/{}/"
            .format(file_name, releases_path, folder_name))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}/{}/web_static/* {}/{}/"
            .format(releases_path, folder_name, releases_path, folder_name))
        run("sudo rm -rf {}/{}/web_static".format(releases_path, folder_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {}/{}/ /data/web_static/current"
            .format(releases_path, folder_name))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
