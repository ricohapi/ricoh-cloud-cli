# -*- coding: utf-8 -*-
# Copyright (c) 2017 Ricoh Co., Ltd. All Rights Reserved.

from setuptools import setup, find_packages
import ricohcloudcli

setup(
    name='ricoh-cloud-cli',
    version=ricohcloudcli.__version__,
    description='Command Line Interface(CLI) for RICOH Cloud API',
    long_description="""Command Line Interface(CLI) for RICOH Cloud API""",
    author='Ricoh Co., Ltd.',
    author_email='',
    url='https://github.com/ricohapi/ricoh-cloud-cli',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'ricoh-cloud-sdk==0.4.0',
        'Click'
    ],
    setup_requires=[
        'pytest-runner',
        'pytest-html'
    ],
    tests_require=[
        'pytest-cov',
        'mock',
        'pytest',
        'pytest-pycodestyle'
    ],
    entry_points={
        'console_scripts':
            ['rapi=ricohcloudcli.cli:main']
    }
)
