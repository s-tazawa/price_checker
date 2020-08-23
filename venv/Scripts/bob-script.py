#!c:\projects\heroku\heroku-buildpack-python\venv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'bob-builder==0.0.18','console_scripts','bob'
__requires__ = 'bob-builder==0.0.18'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('bob-builder==0.0.18', 'console_scripts', 'bob')()
    )
