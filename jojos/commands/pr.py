"""The pr command."""

from subprocess import check_output
from json import dumps

from .base import Base


class Pr(Base):
    """Create pull-request"""

    def run(self):
        print(check_output(['echo', 'hey']))
        print('this is pr town')
        print('You supplied the following options:', dumps(self.options, indent=2, sort_keys=True))
