"""The co command."""
# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import errno
import json
import sys
from subprocess import check_output

from github import UnknownObjectException

from ..utils.github import get_repo
from .base import Base

cache_file = '/tmp/github-7geese-pr-branch-cache.json'


class Co(Base):
    """Checkout correct branch based on pull request number"""

    def run(self):
        try:
            with open(cache_file) as f:
                cache = json.load(f)
        except IOError as ex:
            if ex.errno != errno.ENOENT:
                raise
            cache = {}

        pr_id_str = self.options['<pull_request_id>']
        try:
            pr_id = int(pr_id_str)
        except ValueError:
            print('Not a number: {}'.format(pr_id_str))
            sys.exit(1)

        branch_name = cache.get(pr_id_str)
        if branch_name is None:
            repo = get_repo()
            try:
                pull = repo.get_pull(pr_id)
            except UnknownObjectException:
                print('Could not find a pull request with this ID: {}. Did you already push your branch?'
                      .format(pr_id))
                sys.exit(1)
            branch_name = pull.head.ref
            cache[pr_id_str] = branch_name
            with open(cache_file, b'w') as f:
                json.dump(cache, f, indent=4)

        print(check_output(['git', 'checkout', branch_name]))
