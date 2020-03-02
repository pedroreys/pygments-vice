#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
pygments-vice
~~~~~~~~
pygments-vice is a pygments style that is a port of the vim-vice "Dark and Vibrant colorscheme for vim".

:copyright: Copyright 2020 by Pedro Reys.
:license: MIT, see LICENSE for details.
"""
from setuptools import setup, find_packages

from vice import __version__

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pygments-vice',
    version = __version__,
    url='https://github.com/pedroreys/pygments-vice',
    license='MIT',
    author='Pedro Reys',
    author_email='pedro@pedroreys.com',
    description='pygments-vice is a pygments style that is a port of the vim-vice colorscheme',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='syntax highlighting pygments style',
    packages=find_packages(),
    install_requires=['pygments >= 2.0'],
    entry_points={
            'pygments.styles': ['vice = vice.vice:ViceStyle'],
        },
    platforms='any',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules',
      ]
)
