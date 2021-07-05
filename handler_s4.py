import os
import sys
import hashlib

m = hashlib.md5()
dct = {}
dict_hash = {}
# final_dict = {}
dict_number = {}

def display_duplicates(d_hash):
    global dict_number
    final_dict = {}
    for key, value in d_hash.items():
        if len(value) > 1:
            size_files = os.path.getsize(value[0])

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
                    dict_number[counter] = file_name
                    counter += 1


def delete_files(dict_files_rm):
    ready_rm = None
    print('Enter file numbers to delete: ')
    numbers_rm = input()
    list_keys = list(dict_files_rm.keys())
    list_keys_str = [str(i) for i in list_keys]
    # list_numbers = numbers_rm.split(' ')
    # list_numbers_int = [int(i) for i in list_numbers]
    for num in numbers_rm.split(' '):
        if num in list_keys_str:
            # print('ok')
            ready_rm = True
        else:
            ready_rm = False
            break

    if ready_rm:
        total_free = 0
        list_numbers = numbers_rm.split(' ')
        list_numbers_int = [int(i) for i in list_numbers]
        for num in list_numbers_int:
            size_free = os.path.getsize(dict_files_rm[num])
            total_free += size_free
            os.remove(dict_files_rm[num])

        print(f'\nTotal freed up space: {total_free} bytes')
    else:
        print('Wrong format')



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
            print('Delete files?')
            delete_yes = input()
            if delete_yes == 'yes':
                delete_files(dict_number)
                break
            else:
                break
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
