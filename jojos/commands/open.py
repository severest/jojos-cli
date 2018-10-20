"""The open command."""
from __future__ import absolute_import, division, print_function, unicode_literals

from subprocess import check_output

from ..utils import github
from .base import Base


class Open(Base):
    """Open PR of current branch in browser"""

    def run(self):
        branch_name = check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()
        branch_name = '7Geese:{}'.format(branch_name)
        prs = github.find_prs_for_branch(branch_name)
        if len(prs) > 1:
            pr_ids = sorted('#{}'.format(pr['id']) for pr in prs)
            print('Found several PRs: {}, opening {}'.format(', '.join(pr_ids), pr_ids[0]))
        check_output(['open', prs[0]['html_url']])
