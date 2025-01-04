import asyncio
import time

async def start_strongman(name, power):
    print (f'Strongman {name} has started the competition')
    for i in range(5):
        await asyncio.sleep(1 / power)
        print (f'Strongman {name} lifted ball number {i}')
    print (f'Strongman {name} has ended the competition')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

if __name__ == '__main__':
    asyncio.run(start_tournament())