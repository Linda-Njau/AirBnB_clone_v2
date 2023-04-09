#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_clean(number=0):
    """Delete out-of-date archives."""
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    if len(archives) <= number:
        return

    [archives.pop() for i in range(number)]
    with lcd("versions"):
        for a in archives:
            local("rm ./{}".format(a))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        if len(archives) <= number:
            return

        [archives.pop() for i in range(number)]
        for a in archives:
            run("rm -rf ./{}".format(a))
