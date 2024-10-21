from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime

def main(directory):
    for root, dirs, files in walk(directory):
        for file in files:
            filepath = join(root, file)
            filetime = getmtime(filepath)
            formatted_time = strftime('%d.%m.%y %H:%M', localtime(filetime))
            filesize = getsize(filepath)
            pdir = dirname(filepath)
            print(f'Файл:{file},',
                  f'Путь:{filepath},',
                  f'Размер:{filesize} байт,',
                  f'Время изменения:{formatted_time},',
                  f'Родительская директория:{pdir}')

main('C:\Program Files\Image-Line\FL Studio 2024\Plugins')