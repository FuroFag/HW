from pprint import pprint
import io

def custom_write(file_name, strings):
    strings_positions = {}
    counter = 1
    file = open(file_name, 'w', encoding = 'utf-8')
    for i in strings:
        byte = file.tell()
        file.write(f'{i}\n')
        strings_positions[(counter, byte)] = i.replace('\n', '')
        counter += 1
    file.close()
    print (strings_positions)

custom_write('stuff.txt', ['i cant breathe', 'officer', 'george floyd'])
