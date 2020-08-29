#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Nanda Lau'
NANDA_EMAIL = u'tw.nanda@gmail.com'
SITENAME = u'府城佛教網'
SITEURL = ''
MIRROR_SITEURL = 'http://myweb.ncku.edu.tw/~lsn46/'
PDF_SITEURL = 'http://nanda.online-dhamma.net'

PATH = 'content'

# avoid processing .html files
READERS = {'html': None}

# mix articles and static files in the same place
# @see https://github.com/getpelican/pelican/issues/1587
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['articles', 'extra']
EXTRA_PATH_METADATA = {
  'extra/robots.txt': {'path': 'robots.txt'},
  'extra/CNAME': {'path': 'CNAME'},
  'extra/404.html': {'path': '404.html'},
  'extra/img/yezi.png': {'path': 'favicon.ico'},
}

TIMEZONE = 'Asia/Taipei'

DEFAULT_LANG = u'zh'
LOCALE = 'zh_TW.UTF-8'

# @see http://docs.getpelican.com/en/3.5.0/settings.html#basic-settings
# @see http://docs.getpelican.com/en/3.5.0/settings.html#path-metadata
PATH_METADATA = 'articles/(?P<urlpath>[-a-zA-Z0-9/]*)/(?P<slug>[-a-zA-Z0-9]*)%(?P<lang>[_a-zA-Z]{2,5})\.rst'

# @see http://docs.getpelican.com/en/3.5.0/settings.html#url-settings
ARTICLE_URL = '{urlpath}/{slug}/'
ARTICLE_SAVE_AS = '{urlpath}/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# https://github.com/getpelican/pelican/issues/1513
# {tag}tagName syntax not working now
# content/articles/2012/09/26/python-create-html-element-dynamically%en.rst

THEME = 'theme'

PLUGIN_PATHS = ['plugins']
PLUGINS = ['edit_on_github', 'embed_github_repository_file', 'embed_picasaweb_image']

# my custom setting for HTML meta info
META_KEYWORDS = '府城佛教網, 府城, 佛教, 佛教網, 原始佛教, 南傳, 上座部, 南傳佛教, 上座部佛教, 巴利三藏, 巴利大藏經, 巴利, 法句經'
META_DESCRIPTION = '府城佛教網'

# generate only index.html and pages and articles. (no archives, tags, categories)
#DIRECT_TEMPLATES = ['index']
# use metadata attribute 'order' in page files for ordering
# @see http://docs.getpelican.com/en/3.5.0/settings.html#url-settings
PAGE_ORDER_BY = 'order'
DISPLAY_PAGES_ON_MENU = False

# CONTENT_DIR_URL is the setting for edit_on_github plugin
CONTENT_DIR_URL = u'https://github.com/twnanda/twnanda/tree/master/content'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# custom Jinja2 filter
def hidden_pages_get_page_with_slug_index(hidden_pages):
    for page in hidden_pages:
        if page.slug == "index":
            return page

JINJA_FILTERS = {
    "hidden_pages_get_page_with_slug_index": hidden_pages_get_page_with_slug_index,
}

# Google Custom Search
GOOGLE_CSE = '000759460633137666077:lx1yueta8ju'
