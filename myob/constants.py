from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
MYOB_BASE_URL = 'https://api.myob.com/accountright/'
MYOB_PARTNER_BASE_URL = 'https://secure.myob.com/oauth2/'

AUTHORIZE_URL = 'account/authorize/'
ACCESS_TOKEN_URL = 'v1/authorize/'

DEFAULT_PAGE_SIZE = 400

# Format in which MYOB returns datetimes
# (pymyob won't parse these, but offers the constant for convenience).
DATETIME_FORMATS = ['YYYY-MM-DDTHH:mm:ss', 'YYYY-MM-DDTHH:mm:ss.SSS']
