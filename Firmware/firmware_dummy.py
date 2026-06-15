import time, asyncio
import board, fourwire, busio, digitalio
import epaperdisplay, displayio, vectorio

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

# timekeeping
current_epoch_time = time.time()

# Displayio roots for watch

display_terminal = displayio.CIRCUITPYTHON_TERMINAL

async def keep_time():
    # This is pretty much a test! Super crappy
    asyncio.sleep(60)
    current_epoch_time += 60
    keep_time()

async def update_display():
    pass #idk
    # epaper_display.root_group = idja;mck

keep_time()
