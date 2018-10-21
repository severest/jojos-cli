"""The open command."""
from __future__ import absolute_import, division, print_function, unicode_literals

from subprocess import call

from ..utils import github
from .base import Base


class Merge(Base):
    """
    Squash-merge a PR as GitHub would do it, i.e. by creating a commit with a message like this:

        Make template dropdown animation reusable (#6816)

    """

    def run(self):
        pr_id = self.options['<pull_request_id>']
        pr_data = github.get_pr(pr_id)
        retcode = call(['git', 'merge', '--squash', '--no-edit', 'origin/{}'.format(pr_data['head']['ref'])])
        if retcode != 0:
            exit(retcode)
        retcode = call(['git', 'commit', '-m', '{} (#{})'.format(pr_data['title'], pr_id)])
        if retcode != 0:
            exit(retcode)
