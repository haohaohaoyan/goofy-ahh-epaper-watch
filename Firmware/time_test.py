# little baby test for making sure time runs well

import time, math

current_time = math.floor(time.time())

while True:
    print(time.strftime(f'{current_time} %I %M %S %p', time.localtime(current_time)))
    current_time += 1
    time.sleep(1)