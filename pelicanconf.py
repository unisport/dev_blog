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

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'theme/'

HEADER_COVER = 'theme/images/header.jpg'
SOCIAL = (
    ('twitter', 'https://twitter.com/unisportlife'),
    ('github', 'https://github.com/unisport/'),
    ('facebook', 'https://www.facebook.com/unisportstore'),
)

COLOR_SCHEME_CSS = 'tomorrow_night.css'

AUTHORS_BIO = {
  'razius': {
    'name': 'Silviu Tantos',
    'image': 'https://avatars0.githubusercontent.com/u/1162035?v=3&s=400',
    'website': 'http://razius.com',
    'location': 'Copenhagen',
    'bio': 'Bit herder and brewer of dark magic potions.'
  }
}

CSS_OVERRIDE = ['static/css/override.css']
