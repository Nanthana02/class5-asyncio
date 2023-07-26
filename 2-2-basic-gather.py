import asyncio
import time


#ใช้ async await, asyncio, และ ThreadPoolExecutor เพื่อทำงานแบบแบ่งเป็น thred concurrent
#โดยมี function hello ที่เป็น async ในการทำงานและหน่วงเวลา, function main create and run ทั้งสอง task พร้อมกัน
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

async def main():
    task1 = asyncio.create_task(hello(1)) #return immediately, the task is created
    # await asyncio.sleep(3)
    task2 = asyncio.create_task(hello(2))
    await asyncio.gather(task1, task2)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')
