"""AryaLogger setup.py."""

import os
from setuptools import setup, find_packages

with open('LICENSE.txt') as f:
    LICENSE = f.read()

__version__ = "1.0.0"
VERSION = open(os.path.join('AryaLogger', 'version.py')).read()
# pylint:disable=exec-used
exec(VERSION)


PKGNAME = 'AryaLogger'
URL = 'https://github.com/datacenter/' + PKGNAME
DOWNLOADURL = URL + '/releases/tag/' + str(__version__)

setup(
    name=PKGNAME,
    version=__version__,
    description=('Use the SimpleAciUiLogServer and arya to convert UI REST ' +
                 'API calls to ACI Python SDK code.'),
    long_description=open('README.rst').read(),
    packages=find_packages(),
    url='https://github.com/datacenter/AryaLogger',
    download_url=DOWNLOADURL,
    license=LICENSE,
    author='Mike Timm',
    author_email='mtimm@cisco.com',
    zip_safe=False,
    install_requires=[
        'SimpleAciUiLogServer>=1.1.3',
        'acicobra',
        'arya>=1.1.4'
    ],
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ),
    scripts=[os.path.join('AryaLogger', 'AryaLogger.py')],
    entry_points={
        "console_scripts": [
            "aryalogger=AryaLogger:main",
            "AryaLogger=AryaLogger:main",
        ],
    },
)
