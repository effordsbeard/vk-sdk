#!/usr/bin/env python
from setuptools import setup

setup(
    name='vkapi-sdk',
    version='0.1.0',
    description='This is the Python library for support vkapi.com API.',
    author='Anton Petrov',
    maintainer='Anton Petrov',
    maintainer_email='le4dof@gmail.com',
    url='https://github.com/effordsbeard/vkapi-sdk',
    license='Apache',
    long_description=open("README.md").read(),
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    install_requires=[
        'requests'
    ],
)