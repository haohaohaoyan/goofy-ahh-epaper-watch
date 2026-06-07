# Neutron e-paper watch

I really wanted to make myself a wristwatch that I could use and carry around in everyday life. I wanted something cheaper than that cool-looking CircuitMess watch that also provided more functionality for hardware (so I skipped over the PineTime). 

Current features: 
- 1.54 inch e-paper display
- 2000 mAh Li-po battery which will give around 15-20 hours of battery life (hopefully)
- USB-C charging and data transfer
- ESP32 S3 MINI 1 powered, so it has internect connectivity
- 8-pin IO row, with 1 ground, 1 3.3v, and 6 IO pins.
- 2 IO buttons, labeled A and B in the style of the Game Boy
- Reset and boot buttons for programming
- Hopefully won't explode (IMPORTANT)

Firmware TBD. I'm waiting until I have the hardware to actually test it on. 

Assembly notes (so far): Snip off legs on JST-PH receptacle after soldering

## BOM:

Electronics: (I might change a few links to AliExpress but I feel like these are safer, and shipping will be cheaper when a bunch are from the same source)
|Part|Quantity|Reference|Link|
|---|---|---|---|
|ESP32 S3 MINI 1 microcontroller|1|U1|(Digikey) https://www.digikey.com/en/products/detail/espressif-systems/ESP32-S3-MINI-1-N8/15295890|
|2000 mAh Lithium-ion polymer battery|1|N/A| (Adafruit) https://www.adafruit.com/product/2011|
|1.54 inch e-paper display (no breakout)|1|N/A| (Seeed Studio) https://www.seeedstudio.com/1-54-Monochrome-ePaper-Display-with-200x200-Pixels-p-5776.html|
|24-pin ribbon cable connector, .5mm|1|J5| (LCSC) https://www.lcsc.com/product-detail/C262567.html|
|USB-C right-angle receptacle|1|J4 or USB-C| (LCSC) https://www.lcsc.com/product-detail/C2988369.html|
|SMD push button|4|SW1-4: A, B, BOOT, RESET| (LCSC) https://www.lcsc.com/product-detail/C455280.html|
|MCP73831-OT battery charging IC|1|U2| (Digikey) https://www.digikey.com/en/products/detail/microchip-technology/MCP73831T-2ACI-OT/964301|
|MIC5319-3.3YD5-TR LDO IC|1|U3| (Digikey) https://www.digikey.com/en/products/detail/microchip-technology/MIC5319-3-3YD5-TR/1031162|
|Si1308EDL power MOSFET|1|Q1| (Digikey) https://www.digikey.com/en/products/detail/vishay-siliconix/SI1308EDL-T1-GE3/4876435 [Change to BE3 if out of stock, BE3 is less green but is otherwise identical]|
|0603 SMD orange LED|1|D2| (Digikey) https://www.digikey.com/en/products/detail/ams-osram-usa-inc/LO-Q976-PS-25-0-20-R18/1227953|
|JST-PH 2-pin right-angle receptacle|1|J3| (Digikey) https://www.digikey.com/en/products/detail/jst-sales-america-inc/S2B-PH-K-S/926626| 
|4.7 uF 0805 SMD capacitor|3|C1, C2, C12| Generic component, can be from any source, (Digikey) https://www.digikey.com/en/products/detail/samsung-electro-mechanics/CL21A475KAQNNNE/3886902|
|1 uF 0805 SMD capacitor|13|C3-11, C13-16| Generic component, (Digikey) https://www.digikey.com/en/products/detail/nextgen-components/0805B105K100CC/18677039|
|2k ohm 0402 SMD resistor|1|R3| Generic component, (Digikey) https://www.digikey.com/en/products/detail/yageo/RC0402FR-072KL/2827565|
|4.7k ohm 0402 SMD resistor|2|R1, R2| Generic component, (Digikey) https://www.digikey.com/en/products/detail/yageo/RC0402JR-074K7L/726477|
|3 ohm 0402 resistor|1|R6| Generic component, (Digikey) https://www.digikey.com/en/products/detail/yageo/RC0402FR-073RL/5917684|
|10k ohm 0402 resistor|3|R5, R7, R8| Generic component, (Digikey) https://www.digikey.com/en/products/detail/yageo/AC0402FR-0710KL/5895030|
|500 ohm 0402 resistor|1|R4| Generic component, (Digikey) https://www.digikey.com/en/products/detail/yageo/RT0402FRE07500RL/17011324|
|68 uH SMD inductor|1|L1| Generic component, (LCSC) https://www.lcsc.com/product-detail/C168091.html|
|CDBA340-HF Schottky diode|5|D1, D2-6| (Digikey) https://www.digikey.com/en/products/detail/comchip-technology/CDBA340-HF/3308141|
|(Optional) 1x8 female 2.54mm header pins (for IO)|1|J2/IO pins| (Female is probably the best idea to protect against short circuits) (Digikey, but use anything, really) https://www.digikey.com/en/products/detail/w%C3%BCrth-elektronik/61300811821/17737805|

Non-electronics:
- 3D-printed case (TODO)
- Some kind of stretchy watch band (idk)
- (Optional but probably needed) PCB coating for waterproofing

## Credits:

yassin for looking over my battery circuit and pointing out that I tried to shove 5v into 3v3 (I know I'm an idiot)
Kai Pereira for responding to my questions on the hardware slack and for his Overglade badge which I used as a bit of a reference to make sure I'm not doing anything stupid with the e-paper
Waveshare for their e-paper driver (pretty much dropped in the entire schematic for that, do NOT give me any credit for that)
The OCGC Google Chat (a bunch of my friends) for name help