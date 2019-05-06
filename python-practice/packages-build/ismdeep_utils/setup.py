#!/usr/bin/env python
from setuptools import setup
from ismdeep_utils import __version__ as version

setup(
    name='ismdeep_utils',
    version=version,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        "License :: OSI Approved :: MIT License",
        'Topic :: Utilities',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    description='Some useful utils from ismdeep',
    author='ismdeep',
    author_email='ismdeep@protonmail.com',
    url='https://github.com/ismdeep/ismdeep_utils_py',
    py_modules=['ismdeep_utils'], install_requires=['pytest']
)
