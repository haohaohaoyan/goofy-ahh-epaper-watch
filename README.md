# epaper watch (i haven't decided on a proper name)

I really wanted to make myself a wristwatch that I could use and carry around in everyday life. 

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

## BOM:

- 1x ESP32 S3 MINI 1 microcontroller (U1)
- 1x 2000 mAh Lithium-ion polymer battery ([the one at https://www.adafruit.com/product/1578](https://www.adafruit.com/product/2011)) 
- 1.54 inch e-paper display (display only, without driver, the one at https://www.seeedstudio.com/1-54-Monochrome-ePaper-Display-with-200x200-Pixels-p-5776.html probably)
- 1x 24-pin ribbon cable connector (.5mm gap) (J5)
- 1x USB-C receptacle (look for some LCSC one, horizontal USB-C receptacle) (J4 or USB-C)
- 4x push button (C455280 SMD push button) (SW1-4: A, B, BOOT, RESET)
- 1x MCP73831-OT battery charging IC (U2)
- 1x MIC5319-3.3YD5-TR LDO IC (U3)
- 1x Si1308EDL MOSFET (Q1)
- 1x LED (0603 orange LED) (D2)
- 1x JST-PH connector (J3)
- 3x 4.7 uF 0805 SMD capacitor (C1, C2, C12)
- 13x 1 uF 0805 SMD capacitor (C3-11, C13-16)
- 2x 4.7 ohm 0201 SMD resistor (R1, R2)
- 1x 2k ohm 0201 SMD resistor (R3)
- 1x 3 ohm 0201 resistor (R6)
- 3x 10k ohm 0201 resistor (R5, R7, R8)
- 1x 500 ohm 0201 resistor (R4)
- 1x 68 uH SMD inductor (L1)
- 5x CDBA340-HF Schottky diode (D1, D2-6)
- (Optional) 1x8 2.54mm header pins for IO pins
