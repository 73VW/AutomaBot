"""Automabot bot for Discord."""

from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    setup_requires=['pbr'],
    pbr=True,
    install_requires=(
        'discord.py>=0.16.8',
        'aiohttp>=1.0.0,<1.1.0',
        'pyfiglet>=0.7.5',
        'toml>=0.9.2'
    ),
    entry_points={
       'console_scripts': [
           'automabot = automabot.__main__:main',
       ],
    },
    include_package_data=True
)
