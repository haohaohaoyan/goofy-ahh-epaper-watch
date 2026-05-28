---
title: "goofy epaper watch"
author: "Haoyan Li"
description: "A (hopefully small and battery-light) watch to carry around."
created_at: "2026-05-23"
---

# 5/23: Research & a bit of schematic work

I settled on my idea (a watch powered by a lipo battery with an e-paper display and wireless connectivity to automatically fix time). Since I don't know too much about hardware design asides from super sanitized tutorials, I needed to do some research regarding these things. Looking at footprints in KiCad and photos online, the ESP32 S3 Mini 1 made more sense than the regular ESP32 WROOM for its size. The RP2040 initially looked more convenient but I really wanted that WiFi connectivity for automatic time correction and possibly some weather prediction features. I thought that using the bare chip was also better because it allowed me to connect the data right to the microcontroller while charging the battery that will be powering the rest of the device (at least that's how I'm hoping it will work.) I'm also planning on using a 1.54 inch e-paper display, but I'm trying to avoid using any driver boards to keep the device compact. While doing research, I set up some of the components in KiCad and wired some basic things together (a few wires, and the boot & reset buttons). The debug buttons had to use a pull-down resistor (which I learned about because of the schematic at https://diy.viktak.com/wp-content/uploads/2023/11/esp32-s3-mini-1-schematics.png, because i have NO idea about how to use this thing). I stopped at the battery circuit because that seemed too hard and I wanted to take a break. Afterward, I looked back a bit and did some more looking around at how to power the battery, landing on using a battery charger/power path management IC (but not after messing around with a battery charger WITHOUT power path management for a solid 30 minutes). I've gotten most of the basics done today so far. 

Lapses: https://lapse.hackclub.com/timelapse/2YLNZjLKJ49O, https://lapse.hackclub.com/timelapse/AwMG_Jw_1pwr

![Beginning some work here](Journal/05-23-26.png)

**Total time spent: 1.5 hours**

# 5/24: Pretty much finished up with the power circuit

I gave up on swapping that battery charger/power path management IC (too many pins and I don't wanna deal with that now) and kept the earlier IC (the MCP73831-OT) and instead added two Schottky diodes that would automatically complete the circuit using the source currently active (power supplied from the USB-C input or the battery). Idea was yoinked from some guy on Reddit who was responding to someone with the exact same issue that I had, and also put up the possible issue that the diodes would reduce the battery voltage below 3.3V and make it unusable, so I went through like 20 resistor datasheets one by one before just Googling a low power loss diode and landing on the currently used ones. Everything for the power should be wired up right, but I sent it to the hardware channel on the HC Slack just in case. I'll also start off the README with a BOM so I won't forget anything. Thanks to Kai Pereira on the Slack for helping me with a question about the e-paper thing, which I'll hopefully be doing tomorrow.

Lapse: https://lapse.hackclub.com/timelapse/NfazSZBNFMmf

![Pretty much done with the power circuit](Journal/05-24-26.png)

**Total time spent: 1 hour**

# 5/25: E-paper display driver essentially done, figured out that I need an RTC IC

I don't know how the e-paper drivers work, so I just shoved all of the main junk from the Waveshare e-paper driver HAT onto my PCB. Credits to them for the most part. Obviously, the compatibility switches were taken out because I only need one type of display. Also looked at Kai Pereira's Overglade badge to make sure that I really wasn't doing something stupid with this. It actually took a really long time to figure out exactly what pins to hook the data lines for the EPD to, because all of the ones on this ESP32 are named really confusing things (There were too many options and I didn't know what some were, just that they were SPI.) I also added an A & B button for controlling the watch and wired them to the two pins that weren't used in the middle of all of the currently used ones. The only thing left to do is get the real-time-clock thing settled, because I just realized that CircuitPython can't really keep track of time. I found a good IC for that, and I'll get it wired up tomorrow, if I don't have much schoolwork (which I shouldn't, because it's a party day.)

Lapse: https://lapse.hackclub.com/timelapse/eFtLpvhWv_lq

![E-paper display much original driver such wow](Journal/05-25-26.png)

**Total time spent: 1.2 hours**

# 5/26: LDO added and some RTC connections

I didn't really have much time today due to some other tasks. yas on the #hardware channel looked over my power circuit and pointed out that I was trying to wire 5V directly to the 3V3, which would probably have blown up the entire thing. I fixed that with an LDO IC that's hopefully small enough. I could make it smaller but I chose a moderately larger one because KiCad doesn't have another footprint currently. I also got some of the RTC connections down and made sure that it was compatible with CircuitPython (don't wanna learn c yet). Weirdly enough, like half of the pins on the RTC IC need pull-up resistors, which I haven't seen before. I'll finish that tomorrow. I'm also going to update the BOM to include the new and smaller components. 

Lapse: https://lapse.hackclub.com/timelapse/BdzhmiEXduZc

![Current RTC setup](Journal/05-26-26.png)

**Total time spent: 0.3 hours**

# 5/27: Finished with schematic, some footprint assigning

The schematic is finished! I need to review it and make sure it won't instantly explode but everything should be done! I finished the RTC connections and connected some IO pins to what will be a perfboard-like devboard thing because I don't want all of those microcontroller capabilities to go to waste. The footprints are going to be a pain but I've started assigning a few. The worst part so far is having to make an EasyEDA account to rip footprints off parts that aren't in KiCad's libraries. 

Lapse: https://lapse.hackclub.com/timelapse/oYHkt6sVn5RI

![Full schematic!](Journal/05-27-26.png)

**Total time spent: 0.5 hours**