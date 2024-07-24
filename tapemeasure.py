import time
import board
import busio
import adafruit_tca9548a
import adafruit_vl53l0x
import gc
import math
import time
import framebufferio
import vectorio
import terminalio
import displayio
import adafruit_st7735
import adafruit_st7735r
#import simpleio
#import busio
#from adafruit_display_shapes.rect import Rect
#from adafruit_display_shapes.roundrect import RoundRect
#from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label, wrap_text_to_lines
#from circuitpython_uplot.plot import Plot, color
##################################################################################################################################
displayio.release_displays()
##################################################################################################################################
# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# For each sensor, create it using the TCA9548A channel instead of the I2C object
gammaQuad = adafruit_vl53l0x.VL53L0X(tca[0])
gammaQuad1 = adafruit_vl53l0x.VL53L0X(tca[1])
gammaQuad2 = adafruit_vl53l0x.VL53L0X(tca[7])
gammaQuad3 = adafruit_vl53l0x.VL53L0X(tca[6])
##################################################################################################################################


tft_clk  = board.SCK
tft_mosi = board.MOSI
tft_rst  = board.TX
tft_dc   = board.RX
tft_cs   = board.A3
tft_bl   = board.A2
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)


# Make the displayio SPI bus and the GC9A01 display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = adafruit_st7735r.ST7735R(display_bus, width=132, height=160, backlight_pin=tft_bl)

def set_backlight(val):
    val = max(0, min(1.0, val))
    display.auto_brightness = False
    display.brightness = val
#################################################################################################################################
group = displayio.Group()
display.root_group = group

yellow = 0xC19C00
brightYellow = 0xF9F1A5
white = 0xFFFFFF
red = 0xC50F1F
orange = 0xFF5500
blue = 0x0000FF
pink = 0xFF00FF
purple = 0x881798
brightPurple = 0xB4009E
white = 0xFFFFFF
green = 0x16C60C
aqua = 0x00FFFF
grey = 0x4A4A4A

font = terminalio.FONT

text_f = " "
f_text = label.Label(font, text=text_f, color=white)
f_text.anchor_point = (0.0, 0.0)
f_text.anchored_position = (13, 4)
group.append(f_text)

text_a = " "
a_text = label.Label(font, text=text_a, color=blue)
a_text.anchor_point = (0.0, 0.0)
a_text.anchored_position = (13, 24)
group.append(a_text)

text_r = " "
r_text = label.Label(font, text=text_r, color=orange)
r_text.anchor_point = (0.0, 0.0)
r_text.anchored_position = (13, 44)
group.append(r_text)

text_t = " "
t_text = label.Label(font, text=text_t, color=pink)
t_text.anchor_point = (0.0, 0.0)
t_text.anchored_position = (13, 64)
group.append(t_text)

group.scale = 2

gc.collect()
#################################################################################################################################

gc.collect()

##################################################################################################################################

# After initial setup, can just use sensors as normal.
while True:
    pass
    f_text.text = "F: {0}mm".format(gammaQuad.range)
    a_text.text = "U: {0}mm".format(gammaQuad1.range)
    r_text.text = "L: {0}mm".format(gammaQuad2.range)
    t_text.text = "R: {0}mm".format(gammaQuad3.range)
    gc.collect()
    #set_backlight(1.0)
    #gc.collect()
    #print('Range: {}mm'.format(gammaQuad.range))
    #print('Range1: {}mm'.format(gammaQuad1.range))
    #print('Range2: {}mm'.format(gammaQuad2.range))
    #print('Range3: {}mm'.format(gammaQuad3.range))
    time.sleep(.5)# Write your code here :-)
    


