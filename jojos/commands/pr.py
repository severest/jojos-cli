"""The pr command."""

from subprocess import check_output
from json import dumps

from .base import Base


class Pr(Base):
    """Create pull-request"""

    def run(self):
        issue_id = self.options['<issue_id>']

        print('Checking out staging...')
        print(check_output(['git', 'checkout', 'staging']))
        print(check_output(['git', 'fetch']))
        print('Searching for branches...')
        branches = check_output(['git', 'branch', '-a'])
