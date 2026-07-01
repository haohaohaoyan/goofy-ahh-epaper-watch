# Neutron e-paper watch - (relatively) low-cost interactive e-paper wristwatch for the nerdy

A developer/tech nerd friendly wristwatch powered by an ESP32 S3 MINI 1, uses an e-paper display for power efficiency, and a 2000mAh battery for all-day use. It's supposed to provide both the features that a regular watch is supposed to have, while also having smartwatch functions and IO pins to leverage the power of the ESP32 microcontroller. I really wanted to make myself a wristwatch that I could use and carry around in everyday life. I was initially inspired by that really expensive and prebuilt CircuitMess watch, but it lacked the DIY process and developer tools that I wanted (so no PineTime from Flavortown either). I also was bored and wanted to make another hardware project after Hackpad, and I started noticing how much I needed a watch because I got used to borrowing my mom's and forgetting the time afterward. Plus, it just looks cool. The e-paper screen was added for the power advantage over OLED, not drawing power asides from time changes. It made the driver bit more complex (because I didn't want to occupy more space with a drop-in driver module), but might have some orientation issues. The battery was initially going to be 500mAh, but that was much too little and I chose a much larger battery to carry a charge that should last all day at the cost of more space. I think that this will be a rewarding project and a well-functioning timepiece, but that will be settled after I order. 

Current features: 
- 1.54 inch e-paper display
- 1200 mAh Li-po battery which should have about a full day's worth of life, orange LED charging indicator
- Automatic device sleeping when not used (this takes advantage of the e-paper display to keep displaying time)
- USB-C charging and data transfer
- ESP32 S3 MINI 1 powered, for internet and Bluetooth
- Automatically syncs time with NTP every 6 hours (planned in firmware)
- 8-pin female IO pin row, with 1 ground, 1 3.3v, and 6 IO pins.
- 2 IO buttons, labeled A and B in the style of the Game Boy
- Reset and boot buttons for programming
- Hopefully won't explode (IMPORTANT)
- Hopefully won't revolt and kill me (ALSO IMPORTANT)

Firmware is currently untested (asides from the timekeeping loop) and is only there for submission purposes. It is currently in CircuitPython but I will probably rewrite it in C at one point.

Assembly notes (so far): Snip off legs on JST-PH receptacle after soldering, apply Kapton tape to the side of the battery that will lie in contact with the board, apply Kapton tape to backside of e-paper screen, use DOUBLE SIDED FOAM TAPE??? PCB should snap into case

## Schematic

![schematic image ooh cool](PCB/schematic_image.png)

## PCB
Note: the PCB is 66x36mm

![pcb image ooh cool](PCB/PCB_image.png)

3D render:

![pcb render ooh cool](PCB/PCB_3D_image.png)

## Case

![case image ooh cool](Case/case_image.png)

## BOM in BOM.csv

It comes to $57.66 minimum without shipping, including PCB, stencil, and watch strap. Not great but better than the CircuitMess's $130 and the PebbleTime 2's $225. 

It's probably a good idea to order 1-2 extra of the small components, like the capacitors, resistors, and diodes. The crystal could also have a spare because of how easy it is to fry them.

Also probably needed: PCB conformal coating for waterproofing and Kapton tape

## Extra Credits:

yassin for looking over my battery circuit and pointing out that I tried to shove 5v into 3v3 (I know I'm an idiot) and looking at my crystal

Kai Pereira for responding to my questions on the hardware slack and for his Overglade badge which I used as a bit of a reference to make sure I'm not doing anything stupid with the e-paper

Waveshare for their e-paper driver (pretty much dropped in the entire schematic for that but removed the compability switches, do NOT give me any credit for that) (I cannot stress enough that all credit should go to them because I literally do not know anything about e-paper displays. Like, I understand a bit about what the parts are doing but not too much, really. That's my fault.)

Matters of Intrigue for a good video on the ESP32 S3's timing (https://www.youtube.com/watch?v=fZAR8WTKiSg)

OCGC (a bunch of my friends shoved onto a Google Chat) for name help