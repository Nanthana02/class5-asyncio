import asyncio
import time

#ใช้ async await เพื่อสร้างฟังก์ชันที่ทำงานแบบ async
async def sleep():
    print(f'Time: {time.time() - start:.2f}')
    time.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Task {name}: Computing {total}+{number}')  
        await sleep()
start = time.time()  

#สร้าง event loop 
loop = asyncio.get_event_loop()

#สร้างงานให้กับ event loop โดยใช้ loop.create_task
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]

#run event loop โดยใช้ loop.run_until_complete
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Time: {end-start:.2} sec')

#
# Task A: Computing 0+1
# Time: 0.00
# Task A: Computing 0+2
# Time: 1.02
# Task B: Computing 0+1
# Time: 2.03
# Task B: Computing 0+2
# Time: 3.04
# Task B: Computing 0+3
# Time: 4.05
# Time: 5.1 sec