"""setup.py file."""

import uuid

from setuptools import setup, find_packages

__author__ = 'Matt Ryan <inetuid@gmail.com>'

def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


install_reqs = parse_requirements('requirements.txt')
reqs = [str(ir) for ir in install_reqs]

setup(
    name="napalm-ros",
    version="0.3.1",
    packages=find_packages(),
    author="Matt Ryan",
    author_email="inetuid@gmail.com",
    description="Network Automation and Programmability Abstraction Layer driver for Mikrotik ROS",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS',
    ],
    url="https://github.com/metool/napalm-ros",
    include_package_data=True,
    install_requires=reqs,
)
