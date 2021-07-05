import os
import sys
import hashlib

m = hashlib.md5()
dct = {}
dict_hash = {}
# final_dict = {}

def display_duplicates(d_hash):
    final_dict = {}
    for key, value in d_hash.items():
        if len(value) > 1:
            size_files = os.path.getsize(value[0])
            # print(f"{key}: {value}, {size_files}")

            if size_files in final_dict:
                final_dict[size_files].append(key)
            else:
                final_dict[size_files] = [key]

    counter = 1

    for key, value in final_dict.items():
        print(f"\n{key} bytes")
        for has_key, has_value in d_hash.items():
            if has_key in value:
                print(f'Hash: {has_key}')
                for file_name in has_value:
                    print(f'{counter}. {file_name}')
                    counter += 1


def check_duplicates(value):
    with open(value, "rb") as f:
        bytes = f.read()  # read file as bytes
        readable_hash = hashlib.md5(bytes).hexdigest();
        if readable_hash in dict_hash:
            dict_hash[readable_hash].append(value)
        else:
            dict_hash[readable_hash] = [value]


def sort_dct(r):
    dict_hash.clear()
    list_keys = list(dct.keys())
    list_keys.sort(reverse=r)
    for key in list_keys:
        print(key, 'bytes')
        for val in dct[key]:
            print(val)
            check_duplicates(val)


args = sys.argv
if len(args) != 2:
    print('Directory is not specified')
else:
    frm = input('Enter file format:\n')
    for address, dirs, files in os.walk(args[1]):
        for name in files:
            n = os.path.join(address, name)
            size = os.path.getsize(n)
            if frm == '' or os.path.splitext(n)[1] == '.' + frm:
                if size in dct:
                    dct[size].append(n)
                else:
                    dct[size] = [n]

print('Size sorting options:\n1. Descending\n2. Ascending')
while True:
    option = input('Enter a sorting option:\n')
    if option == '1':
        sort_dct(True)
        print("Check for duplicates?")
        check_dup = input()
        if check_dup == 'yes':
            display_duplicates(dict_hash)
            break
        else:
            break
    elif option == '2':
        sort_dct(False)
        print("Check for duplicates?")
        check_dup = input()
        if check_dup == 'yes':
            display_duplicates(dict_hash)
            break
        else:
            break
    print('Wrong option')
