# -*- coding:utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='trip_sorter',
    version='0.0.1',
    packages=find_packages(
        exclude=["*.tests", "*.tests.*", "tests.*", "tests"]
    ),
    include_package_data=True,
    license='TBD',
    description='Trip sorter',
    classifiers=[
        'Environment :: python',
        'Framework :: pytest',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
    ],
)
