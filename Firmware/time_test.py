# little baby test for making sure time runs well

import time, math, asyncio

current_time = math.floor(time.time())

async def display_time():
    print(time.strftime(f'{current_time} %I %M %S %p', time.localtime(current_time)))

while True:
    asyncio.run(display_time())
    current_time += 1
    time.sleep(1)