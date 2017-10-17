#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Zhenhong(Don) Yang'
SITENAME = 'Don & Zhenhong'
SITEURL = 'http://zhenhongy.github.io'

THEME = "nest"
PATH = 'content/'

EXTRA_HEADER = open('_nb_header.html').read()

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
MAIL = 'zhenhongy_1992@hotmail.com'
TWITTER_USER = 'https://twitter.com/Zhenhong1992'
LINKEDIN_USER = 'https://www.linkedin.com/in/zhenhongyang/'
ABOUT_TEXT = 'Thanks for taking time! Please feel free to share any of your thoughts with me.'
ABOUT_IMAGE = '/Users/zhenhongyang/26512451.jpeg'



# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATH = ['pelican-plugins']
PLUGINS = ['gzip_cache','liquid_tags.notebook','summary']