#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'University of Alberta'
SITENAME = 'CMPUT 404'
SITEURL = ''

PATH = 'content'
THEME = 'templates/cmput404'
TIMEZONE = 'America/Edmonton'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)
LINKS = ()

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)
SOCIAL = ()

DEFAULT_PAGINATION = 20

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'toc_depth': '2-6',
        },
        'markdown.extensions.tables': {},
    },
    'output_format': 'html5',
}
DATE_FORMATS = {
    'en': '%a, %d %b %Y at %H:%M %Z',
}

STATIC_PATHS=[
	]
PAGE_EXCLUDES=STATIC_PATHS
ARTICLE_EXCLUDES=STATIC_PATHS

PATH_METADATA = '(?P<path_no_ext>.*)\..*'
ARTICLE_URL = ARTICLE_SAVE_AS = PAGE_URL = PAGE_SAVE_AS = '{path_no_ext}.html'