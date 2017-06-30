"""The pr command."""
import re
from itertools import count
from pprint import pprint
from subprocess import check_output

from .base import Base

_cookies = None


class Pr(Base):
    """Create pull-request"""

    def run(self):
        issue_id = self.options['<issue_id>']

        print('Checking out staging...')
        print(check_output(['git', 'checkout', 'staging']))
        print(check_output(['git', 'fetch']))
        print('Searching for branches...')
        branches = [line.strip() for line in check_output(['git', 'branch', '-a']).splitlines()]
        pprint(branches)

        counter = count(start=1)
        for number in counter:
            new_branch = 'issues/{}-{}'.format(issue_id, number)
            if new_branch in branches or 'remotes/origin/{}'.format(new_branch) in branches:
                continue
            break

        print(check_output(['git', 'checkout', '-b', new_branch]))
        print(check_output(['git', 'commit', '-m', 'Connect to issue #{}\n\n[ci skip]'.format(issue_id), '--allow-empty']))
        print(check_output(['git', 'push', '-u', 'origin', new_branch]))
        pr_title = raw_input('Enter PR title: ')
        pr_url = check_output(['hub', 'pull-request', '-m', pr_title]).strip()
        pr_id = re.search(r'/pull/(\d+)', pr_url).group(1)
        check_output(['open', pr_url])
