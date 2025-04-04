# Make a Python script that deletes all files in a directory (be careful!)

import os
import glob

files = glob.glob('delete_me/*')
for f in files:
    os.remove(f)