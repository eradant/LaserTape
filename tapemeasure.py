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
#import simpleio
#import busio
#from adafruit_display_shapes.rect import Rect
#from adafruit_display_shapes.roundrect import RoundRect
#from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label, wrap_text_to_lines
#from circuitpython_uplot.plot import Plot, color

# Create I2C bus as normal
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Create the TCA9548A object and give it the I2C bus
tca = adafruit_tca9548a.TCA9548A(i2c)

# For each sensor, create it using the TCA9548A channel instead of the I2C object
#gammaQuad = adafruit_vl53l0x.VL53L0X(tca[0])
#gammaQuad1 = adafruit_vl53l0x.VL53L0X(tca[1])
#gammaQuad2 = adafruit_vl53l0x.VL53L0X(tca[7])
#gammaQuad3 = adafruit_vl53l0x.VL53L0X(tca[6])

displayio.release_displays()

white = 0x881798
font = terminalio.FONT


tft_clk  = board.SCK
tft_mosi = board.MOSI
tft_rst  = board.TX
tft_dc   = board.RX
tft_cs   = board.A3
tft_bl   = board.A2
spi = busio.SPI(clock=tft_clk, MOSI=tft_mosi)


# Make the displayio SPI bus and the display
display_bus = displayio.FourWire(spi, command=tft_dc, chip_select=tft_cs, reset=tft_rst)
display = adafruit_st7735.ST7735(display_bus, width=128, height=160, backlight_pin=tft_bl)

def set_backlight(val):
    val = max(0, min(1.0, val))
    display.auto_brightness = False
    display.brightness = val

group = displayio.Group()
display.root_group = group


############
# Make the display context

color_bitmap = displayio.Bitmap(128, 128, 1)
color_palette = displayio.Palette(1)
color_palette[0] = 0xFF0000

bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
group.append(bg_sprite)

# After initial setup, can just use sensors as normal.
while True:
    pass
    #set_backlight(1.0)
    gc.collect()
    #print('Range: {}mm'.format(gammaQuad.range))
    #print('Range1: {}mm'.format(gammaQuad1.range))
    #print('Range2: {}mm'.format(gammaQuad2.range))
    #print('Range3: {}mm'.format(gammaQuad3.range))
    #time.sleep(1)# Write your code here :-)
    

