import time, epaperdisplay, displayio, board, digitalio, fourwire, busio, asyncio

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

def keep_time():
    pass