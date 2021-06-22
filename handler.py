# Stage 1. Here come the files
# Display full path of the files inside the folder specified as an argument

import sys
import os

args = sys.argv

if len(args) != 2:
    print('Directory is not specified')
else:
    for root, dirs, files in os.walk(args[1]):
        for name in files:
            print(os.path.join(root, name))
