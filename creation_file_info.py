# Program to see creation of a file
import shutil
from pathlib import Path
from time import ctime
import shutil

source = Path(r"C:\Users\NP\PycharmProjects\pythonProject\HERE.py")
target = Path() / "__init__"
# This line let's you creation of dir
# print(ctime(path.stat().st_ctime))

# print(path.read_text())

shutil.copy(source, target)

