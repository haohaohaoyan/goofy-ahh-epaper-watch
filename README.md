# epaper watch (i haven't decided on a proper name)

readme unfinished
planned features: epaper screen, 500mAh lipo battery, esp32 with internet connectivity for weather & time sync, two buttons for interacting, maybe IO spots for interacting with components

Current features: 
- 1.54 inch e-paper display
- 2000 mAh Li-po battery which will give around 15-20 hours of battery life
- USB-C charging and data transfer
- ESP32 S3 MINI 1 powered, so it has internect connectivity
- 8-pin IO row, with 1 ground, 1 3.3v, and 6 IO.
- 2 IO buttons, labeled A and B in the style of the Game Boy
- Reset and boot buttons for programming
- Hopefully won't explode (IMPORTANT)

## BOM:

- 1x ESP32 S3 MINI 1 microcontroller
- 1x 2000 mAh Lithium-ion polymer battery ([the one at https://www.adafruit.com/product/1578](https://www.adafruit.com/product/2011))
- 1.54 inch e-paper display (display only, without driver, the one at https://www.seeedstudio.com/1-54-Monochrome-ePaper-Display-with-200x200-Pixels-p-5776.html probably)
- 1x USB-C receptacle (exact component tbd, horizontal USB-C receptacle)
- 4x push button (C455280 push button)
- 1x MCP73831-OT battery charging IC
- 1x MIC5319-3.3YD5-TR LDO IC
- 1x Si1308EDL MOSFET
- 1x DS3231MZ real-time clock
- 1x LED (0603 orange LED)
- 1x JST-PH connector
- 3x 4.7 uF capacitor (needs to be checked) (all caps are 0805)
- 14x 1 uF capacitor
- 2x 4.7 ohm resistor (needs to be checked) (all resistors are 0603)
- 3x 2k ohm resistor (eh)
- 1x 3 ohm resistor
- 1x 10k ohm resistor
- 1x 500 ohm resistor 
- 1x 68 uH inductor 
- 5x CDBA340-HF Schottky diode
