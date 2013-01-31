from .settings import *

try:
    from .settings_local import *
except ImportError, exc:
    exc.args = tuple(
        ['%s (did you rename settings/settings_local.py?)' % exc.args[0]])
    raise exc
