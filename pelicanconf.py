#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'birbs'
SITENAME = 'names-are-hard'
SITEURL = 'https://arctice.github.io/birb-blog'

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = 'English'

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

THEME = './themes/voce/'

PLUGIN_PATHS = ['./themes/voce/plugins/']
PLUGINS = ['assets']

#JINJA_ENVIRONMENT = {}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
