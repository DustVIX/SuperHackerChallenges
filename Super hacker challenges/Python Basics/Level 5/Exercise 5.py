# Create a script that renames all .txt files in a folder to .bak.

import os

for filename in os.listdir("rename"):
    rename_file = filename.replace(".py","")

    os.rename(f"rename\\{rename_file}.py", f"rename\\{rename_file}.bak")
    print("Done!")