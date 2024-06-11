### Shop name
HYUNSTORYMALL = "현스토리몰"

### get abs
import os
import sys
def resource_path(relpath):
    try:
        abspath = sys._MEIPASS
    except Exception:
        abspath = os.path.abspath(".")
    return os.path.join(abspath, relpath)