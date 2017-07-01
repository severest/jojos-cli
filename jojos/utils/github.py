from __future__ import absolute_import

import os

import yaml
from github import Github


def get_repo():
    github = Github(find_oauth_token())
    return github.get_repo('7Geese/7Geese')


def find_oauth_token():
    hub_config = os.path.join(os.path.expanduser('~'), '.config/hub')
    if not os.path.exists(hub_config):
        return None
    with open(hub_config) as f:
        data = yaml.load(f, Loader=yaml.Loader)
    return data['github.com'][0]['oauth_token']
