import asyncio
import time

#ใช้ async await และ asynciocreate and run hello(i) ทั้งหมด 10 event ที่ทำงานพร้อมกัน
async def hello(i):
    print(f"{time.ctime()} hello {i} started")
    await asyncio.sleep(4)
    print(f"{time.ctime()} hello {i} done")

#สร้าง list ของ coroutine objects เส้นงาน hello(i) ทั้งหมด 10 event
async def main():
    coros = [hello(i) for i in range(10)]  
    await asyncio.gather(*coros)

if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(f'Time: {end-start:.2f} sec')


# Wed Jul 26 15:09:15 2023 hello 0 started
# Wed Jul 26 15:09:15 2023 hello 1 started
# Wed Jul 26 15:09:15 2023 hello 2 started
# Wed Jul 26 15:09:15 2023 hello 3 started
# Wed Jul 26 15:09:15 2023 hello 4 started
# Wed Jul 26 15:09:15 2023 hello 5 started
# Wed Jul 26 15:09:15 2023 hello 6 started
# Wed Jul 26 15:09:15 2023 hello 7 started
# Wed Jul 26 15:09:15 2023 hello 8 started
# Wed Jul 26 15:09:15 2023 hello 9 started
# Wed Jul 26 15:09:19 2023 hello 0 done
# Wed Jul 26 15:09:19 2023 hello 2 done
# Wed Jul 26 15:09:19 2023 hello 6 done
# Wed Jul 26 15:09:19 2023 hello 9 done
# Wed Jul 26 15:09:19 2023 hello 8 done
# Wed Jul 26 15:09:19 2023 hello 5 done
# Wed Jul 26 15:09:19 2023 hello 7 done
# Wed Jul 26 15:09:19 2023 hello 4 done
# Wed Jul 26 15:09:19 2023 hello 1 done
# Wed Jul 26 15:09:19 2023 hello 3 done
# Time: 4.03 sec