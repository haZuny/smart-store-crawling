from cx_Freeze import setup, Executable
import sys

buildOptions = {
	"packages":[
    	'requests','datetime','os','win32gui', 'win32con', "tkinter", "traceback",
        'abc', 'time', 'bs4', 'selenium', 'openpyxl', 'PIL', 'requests'
    ],
    "excludes":[
    	"matplotlib"
    ]
}
 
base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe = [Executable("main.py", base=base)]
 
setup(
    name='main',
    version='2.2',
    author='HadenKwon',
    options = dict(build_exe = buildOptions),
    executables = exe
)