#!/usr/bin/python3
"""
Fabric script that deletes out-of-date archives
"""

from fabric.api import *
from os import listdir, remove
from os.path import isfile, join

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_clean(number=0):
    """
    Deletes all unnecessary archives from versions and releases folders.
    """
    try:
        number = int(number)
        if number < 0:
            return
    except ValueError:
        return

    # Get a list of all archives in versions folder
    with cd("versions"):
        archives = sorted(listdir("."))

    # Delete all unnecessary archives from versions folder
    if number == 0:
        number = 1
    elif number >= len(archives):
        return

    for archive in archives[:-number]:
        if isfile(archive):
            remove(archive)

    # Get a list of all releases from both servers
    with cd("/data/web_static/releases"):
        releases = run("ls -1").split('\n')

    # Delete all unnecessary archives from both servers
    if len(releases) <= number:
        return

    for release in releases[:-number]:
        if release != "test":
            run("sudo rm -rf /data/web_static/releases/{}/".format(release))
