#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Data ramblers'
SITENAME = "Data ramblers' code lair"
SITEURL = ''
SITESUBTITLE = 'Our precious'
CC_LICENSE = 'CC-BY-NC'

PATH = 'content'
STATIC_PATHS = ['assets', 'static']

TIMEZONE = 'Europe/Zurich'

DEFAULT_LANG = 'en'
LOCALE = 'de_CH.utf8'
DATE_FORMATS = {'en': '%Y-%m-%d'}

DEFAULT_CATEGORY = 'blog'

THEME = 'template'
HEADER_COVER = 'assets/background.png'

DISPLAY_BREADCRUMBS = True

PYGMENTS_STYLE = 'zenburn'
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}
TYPOGRIFY = True

PLUGIN_PATHS = ['plugins']
PLUGINS = [
'md_inline_extension',
'simple_footnotes'
]

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

DEFAULT_PAGINATION = 10

SUMMARY_MAX_LENGTH = 30
FILENAME_METADATA = '(?P<date>\d{2}\d{2}\d{2})_(?P<slug>.*)'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
