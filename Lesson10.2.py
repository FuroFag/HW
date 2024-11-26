from datetime import datetime
import multiprocessing

def read_info(name):
    all_data = []
    with open (name, encoding = 'utf-8') as file:
        data = file.readline()
        while data:
            data = file.readline()
            all_data.append(data[0:-1])

filenames = [f'{number}.txt' for number in range(1, 5)]

start = datetime.now()
read_info(filenames[0])
read_info(filenames[1])
read_info(filenames[2])
read_info(filenames[3])
end = datetime.now()
print (f'Линейный вызов занял {end - start}')

if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes = 4) as pool:
        pool.map(read_info, filenames)
    end = datetime.now()
    print(f'Использование многопроцесcного вызова заняло {end - start}')
    