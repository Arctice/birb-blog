AUTHOR = 'birbs'
SITENAME = 'birb plays games'
SITEURL = 'http://birb.uk'

PATH = 'content'

TIMEZONE = 'Europe/London'
DEFAULT_LANG = 'English'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
GOOGLE_ANALYTICS_ID = None
GOOGLE_ANALYTICS_PROP = None

# Blogroll
LINKS = (('Home', SITEURL+'/index.html'),
        ('Uni', 'https://twitter.com/Unis_verse'),
        ('Arc', 'https://twitter.com/rainlife__'),
        )

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 4

THEME = './themes/voce/'

PLUGIN_PATHS = ['./themes/voce/plugins/']
PLUGINS = ['assets']

USER_LOGO_URL = 'http://i.imgur.com/3ANGARn.png'
MANGLE_EMAILS = True
FUZZY_DATES = True  # uses JS to display fancy dates

DISPLAY_CATEGORIES_ON_MENU = True
DISPLAY_PAGES_ON_MENU = True
DEFAULT_CATEGORY = 'Misc'
