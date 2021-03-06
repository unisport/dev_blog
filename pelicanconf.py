#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Unisport'
SITENAME = 'Unisport Engineering'
SITEURL = ''

PATH = 'content'
STATIC_PATHS = ['static']
ARTICLE_PATHS = ['articles']
PAGE_PATHS = ['pages']

TIMEZONE = 'Europe/Copenhagen'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# PYGMENTS_RST_OPTIONS = {'linenos': 'inline'}

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'theme/'

SOCIAL = (
    ('twitter', 'https://twitter.com/unisportlife'),
    ('github', 'https://github.com/unisport/'),
    ('facebook', 'https://www.facebook.com/unisportstore'),
)

# Theme settings
HEADER_COVER = 'static/images/header.jpg'
CSS_OVERRIDE = ['static/css/override.css']
COLOR_SCHEME_CSS = 'monokai.css'
AUTHORS_BIO = {
    'razius': {
        'name': 'Silviu Tantos',
        'image': 'https://avatars0.githubusercontent.com/u/1162035?v=3&s=400',
        'website': 'http://razius.com',
        'location': 'Copenhagen',
        'bio': 'Bit herder and brewer of dark magic potions.',
    },
}
