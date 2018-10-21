"""The hello command."""
# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

from json import dumps

from .base import Base


class Hello(Base):
    """Say hello, world!"""

    def run(self):
        print('Hello, world!')
        print('You supplied the following options:')
        print(dumps(self.options, indent=2, sort_keys=True))
