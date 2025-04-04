# Find the largest file in a directory.

import os
directory = "."
the_largest_file = 0

for root, dirs, files in os.walk(directory):
   for file in files:
      file_path = os.path.join(root, file)
      file_size = os.path.getsize(file_path)
      if file_size > the_largest_file:
        the_largest_file = file_size
        the_largest_file_name = file_path        
print(f"the largest file is {the_largest_file_name}: {the_largest_file} bytes")