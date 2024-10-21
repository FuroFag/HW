from os import walk
from os.path import join, getmtime, getsize, dirname
from time import strftime, localtime

def main(directory):
    for root, dirs, files in walk(directory):
        for file in files:
            path = join(root, file)
            filetime = getmtime(path)
            final_time = strftime('%d.%m.%y %H:%M', localtime(filetime))
            filesize = getsize(path)
            pdir = dirname(path)
            print(f'Файл:{file},',
                  f'Путь:{path},',
                  f'Размер:{filesize} байт,',
                  f'Время изменения:{final_time},',
                  f'Родительская директория:{pdir}')

main('C:\Program Files\Image-Line\FL Studio 2024\Plugins')