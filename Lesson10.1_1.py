from time import sleep
from datetime import datetime
from threading import Thread

def write_words(word_count, file_name):
    file = open(file_name, 'w', encoding = 'utf-8')
    for i in range(word_count):
        file.write(f'Слово номер №{i}\n')
        sleep(0.1)
    file.close()
    print(f'Закончилась запись в файл {file_name}')

timestart = datetime.now()

ex1 = write_words(10, 'example1.txt')
ex2 = write_words(30, 'example2.txt')
ex3 = write_words(200, 'example3.txt')
ex4 = write_words(100, 'example4.txt')

timeend = datetime.now()
result_nonthread = timeend - timestart
print(f'Время работы в обычном режиме составило {result_nonthread}')

thread_timestart = datetime.now()

thread1 = Thread(target = write_words(10, 'example5.txt'))
thread2 = Thread(target = write_words(30, 'example6.txt'))
thread3 = Thread(target = write_words(200, 'example7.txt'))
thread4 = Thread(target = write_words(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

thread_timeend = datetime.now()
thread_timeresult = thread_timeend - thread_timestart
print(f'Время работы потоков составило {thread_timeresult}')

print(f'Разница составила {thread_timeresult - result_nonthread} секунд')