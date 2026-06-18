# little baby test for making sure time runs well

import time, math, asyncio

current_time = math.floor(time.time())

async def display_time():
    # print(time.strftime(f'{current_time} %I %M %S %p', time.localtime(current_time)))
    for i in range(20):
        print("iajsmd;kcm")

# Circuitpy doesn't have perf counter

ideal = time.monotonic()
offset = 0

while True:
    prev = time.monotonic()
    # Run the periodic process
    asyncio.run(display_time())
    # Sleep time with offset subtracted
    time.sleep(60 - (offset))
    # Ideal time assumes that *exactly* one second or minute has passed
    ideal += 60
    # Offset will be the difference between what the time is and what it should be. If the clock is dragging, the offset will be positive and subtracted, and if rushing it will be negative and added. 
    offset = time.monotonic() - ideal
    post = time.monotonic()
    # Print total elapsed time for debug
    print(prev - post)