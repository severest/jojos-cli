"""The open command."""
from __future__ import absolute_import, division, print_function, unicode_literals

from subprocess import check_output
from urllib import quote_plus

import requests

from ..utils.github import find_oauth_token
from .base import Base


class Open(Base):
    """Open PR of current branch in browser"""

    def run(self):
        branch_name = check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD']).strip()
        branch_name = '7Geese:{}'.format(branch_name)
        response = requests.get('https://api.github.com/repos/7Geese/7Geese/pulls?head={}'.format(quote_plus(branch_name)),
                                headers={'Authorization': 'Token {}'.format(find_oauth_token())})
        assert response.status_code == 200, (response.status_code, response.content)
        body = response.json()
        if not body:
            exit('Could not find PR for this branch')
        check_output(['open', body[0]['html_url']])
