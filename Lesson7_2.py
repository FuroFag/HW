from pprint import pprint
import io

def custom_write(file_name, strings):
    strings_positions = {}

    file = open(file_name, 'w', encoding = 'utf-8')
    for i in strings:
        byte = file.tell()
        file.write(f'{i}\n')
    file.close()
    file = open(file_name, 'r')
    counter = 1
    for i in file:
        strings_positions[(counter, byte)] = i.replace('\n', '')
        counter += 1
    file.close()
    return strings_positions

custom_write('stuff.txt', ['i cant breathe', 'officer', 'george floyd'])
