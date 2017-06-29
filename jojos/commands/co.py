"""The co command."""
from __future__ import absolute_import, division, print_function, unicode_literals

import errno
import json
import os
import sys

import yaml
from subprocess import check_output
from github import Github


from json import dumps

from .base import Base

cache_file = '/tmp/github-7geese-pr-branch-cache.json'


class Co(Base):
    """Checkout correct branch based on pull request number"""

    def run(self):
        try:
            with open(cache_file) as f:
                cache = json.load(f)
        except IOError as ex:
            print('[-] Could not find cache file', file=sys.stderr)
            if ex.errno != errno.ENOENT:
                raise
            cache = {}

        pr_id = self.options['<pull_request_id>']
        branch_name = cache.get(pr_id)
        if branch_name is None:
            gh = Github(self.find_oauth_token())
            repo = gh.get_repo('7Geese/7Geese')
            pull = repo.get_pull(int(pr_id))
            branch_name = pull.head.ref
            cache[pr_id] = branch_name
            with open(cache_file, 'w') as f:
                json.dump(cache, f, indent=4)

        print(check_output(['git', 'checkout', branch_name]))

    def find_oauth_token(self):
        hub_config = os.path.join(os.path.expanduser('~'), '.config/hub')
        if not os.path.exists(hub_config):
            return None
        with open(hub_config) as f:
            data = yaml.load(f, Loader=yaml.Loader)
        return data['github.com'][0]['oauth_token']
