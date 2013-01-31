import os
import sys
import site

# prevent errors with 'print' commands
sys.stdout = sys.stderr

# Activate virtualenv
activate_this = os.path.expanduser("{{ ENV_DIR  }}/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# adopted from http://code.google.com/p/modwsgi/wiki/VirtualEnvironments
def add_to_path(dirs):
    # Remember original sys.path.
    prev_sys_path = list(sys.path)

    # Add each new site-packages directory.
    for directory in dirs:
        site.addsitedir(directory)

    # Reorder sys.path so new directories at the front.
    new_sys_path = []
    for item in list(sys.path):
        if item not in prev_sys_path:
            new_sys_path.append(item)
            sys.path.remove(item)
    sys.path[:0] = new_sys_path

add_to_path([
     os.path.normpath('{{ ENV_DIR  }}/lib/python2.5/site-packages'),
     os.path.normpath('{{ ENV_DIR  }}/lib/python2.6/site-packages'),
     os.path.normpath('{{ ENV_DIR  }}/lib/python2.7/site-packages'),
     os.path.normpath('{{ PROJECT_DIR }}'),
])

os.environ['DJANGO_SETTINGS_MODULE'] = 'ocelot.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()