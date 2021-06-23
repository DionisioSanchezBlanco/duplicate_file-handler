# Stage 2. How much does it weigh
# Display full path of the files inside the folder specified as an argument
# You can filter by extension and the order is by size of the files

import sys
import os
from collections import defaultdict
from collections import OrderedDict

# To get the tree of files in root folder
def get_tree(argument, order, f_format):
    dict_folders = defaultdict(list)
    if order == '1':
        order = False
    else:
        order = True

    for root, dirs, files in os.walk(argument, topdown=order):
        for name in files:
            if f_format in name:
                dict_folders[os.path.getsize(os.path.join(root, name))].append(os.path.join(root, name))

    # print(dict_folders)
    if order:
        dict_sort = OrderedDict(sorted(dict_folders.items()))
    else:
        dict_sort = dict_folders
        print(dict_sort)

    for key, value in dict_sort.items():
        print(f"\n{key} bytes")
        for it in value:
            print(it)

def menu():
    print('Enter file format:')
    file_format = input()
    print('Size sorting options:\n1. Descending\n2. Ascending\n')
    print("Enter a sorting option: ")
    option = input()
    if option not in ['1', '2']:
        print('Wrong option')
    else:
        get_tree(args[1], option, file_format)


args = sys.argv

if len(args) != 2:
    print('Directory is not specified')
else:
    menu()

