# This program is placed into the public domain.
"""
Get the current version number.

If in a git repository, it is the current git tag.
Otherwise it is the one contained in the PKG-INFO file.
To use this script, simply import it in your setup.py file
and use the results of get_version() as your package version:
    from version import *
    setup(
        ...
        version=get_version(),
        ...
    )

Based on this code from Pwithnall :
https://gist.github.com/pwithnall/7bc5f320b3bdf418265a
"""

__all__ = ('get_version')

import subprocess


def get_version():
    """Return last git tag."""
    minor_version = check_output(['git', 'rev-list',
                              '--count', 'master']).decode('latin-1').strip()
    print(minor_version)
    cmd = 'git tag -l [0-9]* "https://github.com/73VW/AutomaBot"'.split()
    try:
        version = subprocess.check_output(cmd).decode().strip()
    except subprocess.CalledProcessError as e:
        print(e.output)
        print('Unable to get version number from git tags')
        exit(1)

    print(str(version[0]))
    print("ok")
    exit(1)

    return version


if __name__ == '__main__':
    print(get_version())
