#!/usr/bin/env python

from distutils.core import setup

setup(
    name='lbrc_edge',
    version='1.0',
    description='NIHR Leicester BRC Edge Models',
    author='Richard Bramley',
    author_email='rabramley@gmail.com',
    url='https://github.com/LCBRU/lbrc_edge/',
    packages=['lbrc_edge'],
    install_requires=[
        'Flask',
        'flask_sqlalchemy',
    ],
)