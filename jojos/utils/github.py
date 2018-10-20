# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals

import os

import requests
import yaml
from github import Github
from six.moves.urllib.parse import quote_plus


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


def request(method, url, **kwargs):
    kwargs.setdefault('headers', {})['Authorization'] = 'Token {}'.format(find_oauth_token())
    return requests.request(method, url, **kwargs)


def find_prs_for_branch(branch_name):
    response = request(
        'GET',
        'https://api.github.com/repos/7Geese/7Geese/pulls?head={}'.format(quote_plus(branch_name)))
    assert response.status_code == 200, (response.status_code, response.content)
    pr_data = response.json()
    if not pr_data:
        exit('Could not find PR for this branch')
    return pr_data


def get_pr(pr_id):
    response = request(
        'GET',
        'https://api.github.com/repos/7Geese/7Geese/pulls/{}'.format(quote_plus(pr_id)))
    assert response.status_code == 200, (response.status_code, response.content)
    return response.json()
