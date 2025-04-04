#  Write a script that compresses a file into a ZIP archive.

from zipfile import ZipFile , ZIP_DEFLATED 

zip_path = "./ZIP files/text.zip"
file_to_zip = "./ZIP files/text.txt"

with ZipFile(zip_path,"w", ZIP_DEFLATED) as zip:
    zip.write(file_to_zip)