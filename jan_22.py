from zipfile import ZipFile
from pathlib import Path

# with ZipFile("zipped_files.zip", "w") as zip:
#     for path in Path("ecom").rglob("*.*"):
#         zip.write(path)
#Here we zipped a folder

with ZipFile("zipped_files.zip") as zip:
    print(zip.namelist())
    info = zip.getinfo("ecom/__init__.py")
    print(info.file_size)
# Here we get info of zipped file
