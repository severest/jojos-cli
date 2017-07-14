"""Simple util to open a URL in the browser."""
# coding=utf-8

from subprocess import check_output


def open_pr_url(pr_url):
    print('Opening {}'.format(pr_url))
    check_output(['open', pr_url])
