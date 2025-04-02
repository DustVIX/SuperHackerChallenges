# Use Python’s uuid module to generate a random device ID.

import uuid

myuuid = uuid.uuid4()
print('Your UUID is: ' + str(myuuid))