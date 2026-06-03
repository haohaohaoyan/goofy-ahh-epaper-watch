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

# 5/28: Just a tad bit of footprint assignment

No time today, and I wanted to keep my streak. I just assigned some more footprints today, tried to import a button footprint, and found a good one for all of the capacitors. Not much. No lapse because I didn't bother to make one.

![Some footprint assignments](Journal/05-28-26.png)

**Total time spent: 0.1 hours**

# 5/29: Footprint assignment finished and starting on PCB

End of year stuff's been going on, but I decided to pull some extra time to work. I actually finished all of the footprint assigning and started on the PCB! This is my favorite part, because I just need to think about placement and mindlessly wiring stuff together. I'll also need to write down those components because I am GOING to forget them. I still need to fix some components, such as choosing the wrong size for the IO pins and having a vertical USB-C plug instead of a horizontal USB-C receptacle, but I'll get to that tomorrow (during summer break YAYA). EVERY SINGLE LAST PIN on the 24-pin ribbon cable got detached because of pin value mismatch so I'm going to have to do that by hand later. I don't have a lapse today (was only going to make a small tweak but worked longer than I expected).

![The PCB so far](Journal/05-29-26.png)

**Total time spent: 0.5 hours**

# 5/30: PCB routing *almost* finished!!!

I know it's 12:00 AM on 5/31, but let me have this one because I really like PCB routing and kinda zoned out while doing it. Anyway, I have now ALMOST FINISHED EVERYTHING!!!!! Everything except the reset and boot buttons have been placed and it looks good so far. I also had some more issues brought up (because I am extremely incompetent) and I got those fixed. I even printed out a 1:1 copy of it and the scale seems ok. I was initially going to add the holes for the wrist strap directly into the PCB, but I'm probably going to go with a printed case instead with the added benefit of more battery protection. I actually did not take into account how cramped this would be with the (relatively) enormous Schottky diodes. The back is left empty save for traces and vias on purpose because the battery's going there and I don't think it's a good idea. I'll probably have to squeeze the reset and boot buttons on there, but I already have an outline where the battery will be so it shouldn't be an issue getting around it. Routing is satisfying, but fitting everything is a headache. I actually contemplated rotating the microcontroller 180 degrees for some convenience before realizing that it would make a WHOLE lot of traces cross over each other and that isn't a good idea. Another challenge was getting around the large Schottky diodes, but it was pretty much fine after I gave up and shoved three of them under the e-paper display. After figuring out the boot button placement, it's just the silkscreens before I can move onto ordering and assembling. 

Lapse: https://lapse.hackclub.com/timelapse/GY0gmqQjs46F

![The PCB, almost complete](Journal/05-30-26.png)

**Total time spent: 3.5 hours**

# 5/31: Squeezed that last boot button in, made some silkscreen icons

I actually got that last button in by rewiring the IO pin connections to give just enough space for it. Even then, I had to put its resistor pretty far and added 3 entire vias to deal with it because there were loads of things in the way, most prominently the battery covering 90% of the backside again. Since everything else is done now and I hopefully won't have to reload the schematic, I started renaming things, changing silkscreens, and adding icons. The IO pins were renamed for clarity and the ESP32 has its name fully written out because that looks really cool. I also added button names for those two IO buttons (that look kinda like the Game Boy ones on purpose), a lightning symbol next to the charging LED, and a silly star icon I have slapped onto like half everything I make. I really am so close to production, but I need to cover the back with silkscreens so it will look *beautiful*. 

Lapse: https://lapse.hackclub.com/timelapse/xiC5fP980MSw

![Wowee silkscreens](Journal/05-31-26.png)

**Total time spent: 0.8 hours**

# 6/1: More silkscreen work and some extra PCB checking

I wanted to finish that PCB art but some things popped up. While checking over my circuit again and scrolling electronics shorts, I thought to check whether the LDO was supplying enough milliamps for when the ESP32 needs to access the internet, because apparently it needs upwards of 300mA for that and my current LDO could only supply 250. I switched it with another one that could handle 500mA that thankfully had the exact same footprint and pinout. I also considered thickening the power traces, but apparently they were already thick enough for my 5V and 3V3 lines. I almost forgot about connecting the ground of the BOOT button with the main pour, so I did that. Most of the work today was on the silkscreens. I added labels to all of the IO pins, recreated the backside in Affinity for design later, and added my own logo onto it. I asked the group chat of my friends, the lounge channel on the HC slack, and a Discord I was in for name ideas because I was somewhat stuck and needed one for the silkscreen art. The group chat tried naming it "tinkerbella" and "jank" (which was a good idea), the one guy on the slack agreed with one person in my group chat on "bernie" (which is the current nickname), and nobody responded on the Discord. For the final name, I settled on Neutron between that and Gearturner (by asking the other nerds in the groupchat again). I worked on the logo plenty and it went quite slowly because I'm horrible with Affinity but I don't have any other vector art softwares. I stopped at finishing the main concept and sent it to the groupchat for approval from the council. I'm going to wait until tomorrow to make a final verdict on that, because the only person who responded told me to change the font and "make it preppy" (her words). 

Lapse: https://lapse.hackclub.com/timelapse/4CGUG4vbtZhq

![Current logo](Journal/06-01-26.png)

**Total time spent: 1 hour**

# 6/2: A lot of work on the back art and getting rid of the RTC IC

That was a pretty big one. As it turns out, I never needed the RTC IC and should've done more research beforehand, because the ESP32 I'm using already has one built in. It's not as accurate, but periodically syncing it with NTP every 12 hours will make it virtually nothing. Thus, I tossed it (and its three resistor and one capacitor lackeys) right out the window and erased it to make space for some art or something. I don't know yet. I'm asking the group chat about that. Also, more work on the silkscreen art because I want my things to look good. I finished up the logo and made most of the art on the backside, which involved going into Blender (which I am actually OK at) and messing around with outline shaders (which I am NOT OK at). It's not too complex right now but I'm looking to add details. At the moment, it's my name, the Hack Club flag, some big splash art, and the logo on the back. Next will be finishing the art on the front. I needed something to occupy my time with anyway because I'm going to ask for (peer?) review at a local makerspace on Thursday, which is also where I'm hoping to find a hotplate for soldering the microcontroller (I only have a cheap soldeirng iron from Hackpad). I should be finishing up with the silkscreens tomorrow. I have images of the front & back sides of the watch, but Kicad's 3D viewer doesn't agree with my edge cuts right now so it's just a rectangle instead of the actual shape.

Lapse: https://lapse.hackclub.com/timelapse/_bV2QoX63d5C

![PCB 3D model front](Journal/06-02-26(1).png)
![PCB 3D model back](Journal/06-02-26(2).png)

**Total time spent: 1.5 hours**