#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jackson Ninly'
SITENAME = u'ninly&rsquo;s bog'
SITEURL = 'http://ninly.github.io'
DESCRIPTION = 'A nice, quiet bog; I mean blog'
EMAIL_ADDRESS = 'j@ninly.net'
GITHUB_ADDRESS = 'http://github.com/ninly'
TWITTER_ADDRESS = 'http://twitter.com/ninly'

TIMEZONE = 'CST6CDT'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = '%d %B %Y'

THEME = '/home/ninly/proj/blog/themes/cebong-dark'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
TAG_FEED_ATOM = 'feeds/tag/%s.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('illruminations', 'http://illruminations.com/'),
          ('commandlinefu.com', 'http://www.commandlinefu.com/'))

# Social widget
SOCIAL = (('github', 'https://github.com/ninly'),
          ('twitter', 'https://twitter.com/ninly'),
          ('g+', 'https://plus.google.com/+JasonConklin'),
          ('last.fm', 'https://last.fm/ninly'),
          ('tumblr', 'https://ninly.tumblr.com'),
          ('soundcloud', 'https://soundcloud.com/ninly'),
          ('bandcamp', 'https://semiautomaticgroundenvironment.bandcamp.com'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## Settings lifted from Terri Yu (terriyu.info)
# Formatting for urls

ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"
SHOW_ARTICLE_AUTHOR = False

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORY_ON_MENU = False

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

# Generate yearly archive

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

