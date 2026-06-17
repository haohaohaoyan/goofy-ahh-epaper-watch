# little baby test for making sure time runs well

import time, math, asyncio

current_time = math.floor(time.time())

async def display_time():
    # print(time.strftime(f'{current_time} %I %M %S %p', time.localtime(current_time)))
    for i in range(20):
        print("iajsmd;kcm")

# Circuitpy doesn't have perf counter

start_time = time.monotonic()
prev = start_time
offset = 0
post = time.monotonic()

for i in range(5):
    # Run the periodic process
    asyncio.run(display_time())
    # debug
    print(time.monotonic() - prev)
    # Sleep time adjusted to account for missing time 
    time.sleep(1 - (time.monotonic() - (post - 1)))
    # past_runtime = time.monotonic() - prev
    # offset = past_runtime - 1
    post = prev 
    prev = time.monotonic()

end_time = time.monotonic()
print(end_time - start_time)
print(f'Total: {(end_time - start_time) * 72}')