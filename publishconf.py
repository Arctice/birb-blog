AUTHOR = 'birbs'
SITENAME = 'birb plays games'
SITEURL = 'http://birb.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'English'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
AUTHOR_FEED_ATOM = 'feeds/by_%s.atom.xml'
FEED_ALL_RSS = 'feeds/all.rss'
CATEGORY_FEED_RSS = 'feeds/%s.rss'
AUTHOR_FEED_RSS = 'feeds/by_%s.rss'
GOOGLE_ANALYTICS = 'UA-97540243-1'
GOOGLE_ANALYTICS_ID = 'UA-97540243-1'
GOOGLE_ANALYTICS_PROP = 'birb-blog'

# Markdown extensions
MARKDOWN = {'extension_configs':{
                #'markdown.extensions.footnotes': {}, broken as hell
                'markdown.extensions.tables': {},
                'markdown.extensions.nl2br': {},
                'markdown.extensions.sane_lists': {},
                'markdown.extensions.toc': {},
                }
        }

DEFAULT_METADATA = {
    'status': 'draft',
}

# Blogroll
LINKS = (('Home', SITEURL+'/index.html'),
        ('Uni', 'https://twitter.com/Unis_verse'),
        ('Arc', 'https://twitter.com/rainlife__'),
        )

# Social widget
SOCIAL = (
  ('RSS', 'http://birb.uk/feeds/all.rss'),
  ('Atom', 'http://birb.uk/feeds/all.atom.xml'),
)

DEFAULT_PAGINATION = 4

THEME = './themes/voce/'

PLUGIN_PATHS = ['./themes/voce/plugins/']
PLUGINS = ['assets']

USER_LOGO_URL = SITEURL+'/images/header_birb.png'
MANGLE_EMAILS = True
FUZZY_DATES = True  # uses JS to display fancy dates

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DEFAULT_CATEGORY = 'Misc'

