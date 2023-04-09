#!/usr/bin/python3
"""
This is a fabric script that generates a tgz archive
"""

from datetime import datetime
from fabric.api import local
from os.path import isdir


def do_pack():
    """
    function to generate a .tgz archive from web_static
    """
    try
        now = datetime.now().strftime('%Y%m%d%H%M%S')
        if not isdir('versions'):
            local('mkdir versions')
        archive_name = 'web_static_{}.tgz'.format(now)
        local('tar -cvzf versions/{} web_static'.format(archive_name))
        return 'versions/{}'.format(archive_name)
    except:
        return None
