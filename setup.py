#!/usr/bin/env python
# -*- test-case-name: twistedchecker -*-
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from setuptools import find_packages, setup


setup(
    name='TwistedChecker',
    description='A Twisted coding standard compliance checker.',
    version='16.0',
    author='Twisted Matrix Laboratories',
    author_email='twisted-python@twistedmatrix.com',
    url='https://github.com/twisted/twistedchecker',
    packages=find_packages(),
    package_data={
        "twistedchecker": ["configuration/pylintrc"]
    },
    entry_points={
      "console_scripts": [
          "twistedchecker = twistedchecker.core.runner:main"
      ]
    },
    license='MIT',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Topic :: Software Development :: Quality Assurance"
    ],
    keywords=[
        "twisted", "checker", "compliance", "pep8"
    ],
    install_requires=[
        "pylint == 1.5.5",
        "logilab-common == 1.2.1",
        "pep8 == 1.7.0",
    ],
    extras_require = {
        'dev':  [
            'twisted>=15.0.0',
            'pyflakes==0.8.1',
            ],
    },
    long_description=open('README.rst').read()
)
