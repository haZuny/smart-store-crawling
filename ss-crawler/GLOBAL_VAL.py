### Shop name
NaverSmartStoreCralwer = "네이버스마트스토어"

### get abs
import os
import sys
def resource_path(relpath):
    try:
        abspath = sys._MEIPASS
    except Exception:
        abspath = os.path.abspath(".")
    return os.path.join(abspath, relpath)