"""Packaging settings."""
from __future__ import absolute_import, division, print_function, unicode_literals

from codecs import open
from os.path import abspath, dirname, join
from subprocess import call

from setuptools import Command, find_packages, setup

from jojos import __version__


this_dir = abspath(dirname(__file__))
with open(join(this_dir, 'README.rst'), encoding='utf-8') as file:
    long_description = file.read()


class RunTests(Command):
    """Run all tests."""
    description = 'run tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(['py.test', '--cov=jojos', '--cov-report=term-missing'])
        raise SystemExit(errno)


setup(
    name='jojos-cli',
    version=__version__,
    description='A jojo command line program in Python.',
    long_description=long_description,
    url='https://github.com/severest/jojos-cli',
    author='Sean Everest',
    author_email='me@seaneverest.com',
    license='UNLICENSE',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='cli',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'PyGithub',
        'docopt',
        'pyyaml',
        'requests',
        'six',
    ],
    extras_require={
        'test': ['coverage', 'pytest', 'pytest-cov'],
    },
    entry_points={
        'console_scripts': [
            'jojos=jojos.cli:main',
        ],
    },
    cmdclass={'test': RunTests},
)
