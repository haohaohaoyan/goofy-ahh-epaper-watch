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
current_face = "watch"

async def update_time():
    pass

async def sync_time():
    pass

# Main time loop & setting

async def open(page):
    # NOT preinitialized, because you can't just construct a displayio group in just one statement like a dictionary. You have to append them???? They're cobbled together when needed.
    face = displayio.Group()
    match page:
        case "watch":
            face.append()
            epaper_display.root_group = face


async def keep_time():
    # Sleep time with offset subtracted
    await asyncio.sleep(60 - (offset))
    # Ideal time assumes that *exactly* one second or minute has passed. Watch formats ideal time for displaying
    ideal_time += 60
    # Run the periodic process so that we can use the updated time
    asyncio.create_task(update_time())
    # Offset will be the difference between what the time is and what it should be. If the clock is dragging, the offset will be positive and subtracted, and if rushing it will be negative and added. 
    offset = time.monotonic() - ideal_time
