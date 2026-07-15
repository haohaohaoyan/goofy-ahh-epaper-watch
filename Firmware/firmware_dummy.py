# big dummy firmware thing that theoretically works in circuitpy but i'm gonna have to rewrite in c anyway for performance
# This probably isn't going to work. Everything is sloppily put together with what CircuitPython can do right now and the menu 
# isn't functioning but it's just a bunch of extra functions for when that's necessary. Hold B for a minute to sync NTP, I guess.
# I'll probably have to rewrite in C for attachInterrupt anyway

import time, asyncio
import board, fourwire, busio, digitalio
import epaperdisplay, displayio, vectorio, terminalio
from adafruit_display_text import label
import os, wifi, rtc, socketpool
import adafruit_ntp # not in base circuitpy

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

# io buttons

button_a = digitalio.DigitalInOut(board.IO26)
button_a.direction = digitalio.Direction.INPUT
button_a.pull = digitalio.Pull.UP

button_b = digitalio.DigitalInOut(board.IO21)
button_b.direction = digitalio.Direction.INPUT
button_b.pull = digitalio.Pull.UP

# wifi things

wifi_ssid = os.getenv("CIRCUITPY_WIFI_SSID")
wifi_password = os.getenv("CIRCUITPY_WIFI_PASSWORD")

# important variables

ideal_time = time.monotonic()
actual_time = 0 # Replace with the ACTUAL time on NTP sync
current_face = "watch"

current_selection = "watch"

# Function that updates time and the watch face to match
async def update_time():
    actual_time += 60
    if current_face == "watch":
        time_string = time.strptime("%H:%M %p", time.localtime(actual_time))
        face = displayio.Group()
        face.append(label.Label(terminalio.FONT, time_string, 0x000000))

# Function for syncing NTP

async def sync_ntp():
    face = displayio.Group()

    try:
        # RTC module isn't included yet, that's in a package and this was from when the external crystal was automatically supported
        wifi.radio.connect(wifi_ssid, wifi_password)
        ntp = adafruit_ntp.NTP(socketpool.SocketPool(wifi.radio), tz_offset=5, cache_seconds = 3600) # 1 hour cache is dummy, will be called once and reinitialized every 6 hours for now
        rtc.RTC().datetime = ntp.datetime
        actual_time = ntp.datetime
        del ntp
        # Actual time & monotonic are from some random point in time, so ideal is reset instead
        ideal_time = time.monotonic() # 12am coding moment
    except ConnectionError:
        face.append(label.Label(terminalio.FONT, "CONNECTION ERROR", 0x000000))


    
    time_string = time.strptime("%H:%M %p", time.localtime(actual_time))
    face = displayio.Group()
    face.append(label.Label(terminalio.FONT, time_string, 0x000000))
    face.append(label.Label(terminalio.FONT, "NTP SYNCED!", 0x000000))
    # update display to say stuff


# Main time loop & setting

async def open(page):
    # NOT preinitialized, because you can't just construct a displayio group in just one statement like a dictionary. You have to append them???? They're cobbled together when needed.
    global current_face
    face = displayio.Group()
    match page:
        case "watch":
            face.append(label.Label(terminalio.FONT, str(actual_time), 0x000000)) # bad bc i dont wanna spend too much time on this
            current_face = "watch"
            epaper_display.root_group = face
        case "menu":
            pass # pretend this opens the menu
        case "sync":
            sync_ntp()
            # sync time with ntp (not really done)



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
    # tick time
    asyncio.run(keep_time())

    # check every second if button B is pressed and not on menu, if so will open menu
    if not button_b.value and current_face != "menu": # syncs NTP instead for testing
        # open("menu")
        sync_ntp()
    # button functions for menu (i friggin miss event listeners)
    elif current_face == "menu":
        if not button_b.value:
            pass # change selection
        elif not button_a.value:
            pass # select
    # The buttons should be tracked with attachInterrupts in C. For now, the program checks them once per second when the asyncio clock sleeps. 
