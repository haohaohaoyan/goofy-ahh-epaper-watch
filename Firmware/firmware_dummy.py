# big dummy firmware thing that theoretically works in circuitpy but i'm gonna have to rewrite in c anyway for performance

import time, asyncio
import board, fourwire, busio, digitalio
import epaperdisplay, displayio, vectorio, terminalio
from adafruit_display_text import label

# initialize epaper display
epaper_bus = fourwire.FourWire(
    spi_bus = busio.SPI(clock = board.IO36, MOSI = board.IO35), 
    command = board.IO33, 
    chip_select = board.IO34, 
    reset = board.IO11
    )

epaper_display = epaperdisplay.EPaperDisplay(
    display_bus = epaper_bus, 
    width = 200, 
    height = 200,
    ram_width = 25,
    ram_height = 25,
    busy_pin = board.IO10
    )

# important variables

ideal_time = time.monotonic()
actual_time = 0 # Replace with the ACTUAL time on NTP sync
current_face = "watch"

# Function that updates time and the watch face to match
async def update_time():
    actual_time += 60
    if current_face == "watch":
        time_string = time.strptime("%H:%M %p", time.localtime(actual_time))
        face = displayio.Group()
        face.append(label.Label(terminalio.FONT, time_string, 0x000000))

# Main time loop & setting

async def open(page):
    # NOT preinitialized, because you can't just construct a displayio group in just one statement like a dictionary. You have to append them???? They're cobbled together when needed.
    global current_face
    face = displayio.Group()
    match page:
        case "watch":
            face.append(label.Label(terminalio.FONT, actual_time, 0x000000)) # bad bc i dont wanna spend too much time on this
            current_face = "watch"
            epaper_display.root_group = face
        case "menu":
            pass # pretend this opens the menu
        case "sync":
            pass # sync time with ntp


async def keep_time(): # constantly running loop that tracks time with time.monotonic and updates the actual time which is fetched from ntp accordingly
    # Sleep time with offset subtracted
    await asyncio.sleep(60 - (offset))
    # Ideal time assumes that *exactly* one second or minute has passed. Watch formats ideal time for displaying
    ideal_time += 60
    # Run the periodic process so that we can use the updated time
    asyncio.create_task(update_time())
    # Offset will be the difference between what the time is and what it should be. If the clock is dragging, the offset will be positive and subtracted, and if rushing it will be negative and added. 
    offset = time.monotonic() - ideal_time


# On startup: open watchface, sync with NTP (assuming from poweroff), start timekeeping
asyncio.create_task(open("watch"))
while True:
    asyncio.run(keep_time())

# Pretend there's attachInterrupts for when the buttons need to be pressed. 