from uber.common import *
from ._version import __version__

barcode_scanning_config = parse_config(__file__)
template_overrides(join(barcode_scanning_config['module_root'], 'templates'))
static_overrides(join(barcode_scanning_config['module_root'], 'static'))

c.JAVASCRIPT_INCLUDES.append('../static/includes/badge_num_barcode.js')