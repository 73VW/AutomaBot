"""Automabot bot for Discord."""

from os import path
from setuptools import setup, find_packages


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='automabot',
    version='0.1.3.dev20170604',  # see PEP-0440
    python_requires='>=3.6',
    author='Maël Pedretti & Chea Dany',
    author_email='mael.pedretti@he-arc.ch & dany.chea@he-arc.ch',
    url='https://github.com/73VW/AutomaBot',
    license='https://opensource.org/licenses/BSD-3-Clause',
    description=__doc__,
    long_description=long_description,
    packages=find_packages(exclude=('contrib', 'docs', 'tests')),
    keywords='discord asyncio bot',
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Home Automation'
    ),
    install_requires=(
        'discord.py>=0.16.8',
        'aiohttp>=1.0.0,<1.1.0',
        'pyfiglet>=0.7.5',
        'toml>=0.9.2'
    ),
    extras_require={
        'fast': ('cchardet', 'aiodns'),  # making it faster (recommended)
        'qa': ('flake8', 'isort', 'pycodestyle', 'pydocstyle', 'rstcheck'),
        'docs': ('Sphinx>=1.6.0', 'sphinxcontrib-trio')
    },
    entry_points={
       'console_scripts': [
           'automabot = automabot.__main__:main',
       ],
    },
    include_package_data=True
)
