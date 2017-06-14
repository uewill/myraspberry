#!/usr/bin/python/
# coding: utf8
import threading
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Image
import ImageDraw
import ImageFont

# Raspberry Pi pin configuration:
RST = 17
# Note the following are only used with SPI:
DC = 27
SPI_PORT = 0
SPI_DEVICE = 0

# 128x64 display with hardware SPI:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST, dc=DC, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=8000000))

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing. Make sure to create image with mode
# '1' for 1-bit color.
width = disp.width
height = disp.height
def  showTime():

    image = Image.new('1', (width, height))

    # Get drawing object to draw on image.
    draw = ImageDraw.Draw(image)

    # Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)

    # Draw some shapes.
    # First define some constants to allow easy resizing of shapes.
    padding = 1
    top = padding
    x = padding
    # Load default font.
    #font = ImageFont.load_default()

    # Alternatively load a TTF font.
    # Some other nice fonts to try: http://www.dafont.com/bitmap.php
    fontTitle = ImageFont.truetype('/usr/share/fonts/truetype/wqy/msyh.ttc', 15)
    font = ImageFont.truetype('/usr/share/fonts/truetype/wqy/msyh.ttc', 30)

    # Write two lines of text.
    #draw.text( (x,padding), u'你好,世界!',font=font, fill=255)
    #draw.text( (x,padding+10), width+"---"+height,font=font, fill=255)
    #draw.text( (x,padding), '1234',font=font, fill=255)
    draw.text( (x,0), time.strftime('%Y-%m-%d',time.localtime(time.time())),font=fontTitle, fill=255)    

    draw.text( (x,padding+10), time.strftime('%H:%M:%S',time.localtime(time.time())),font=font, fill=255)

    #image.save('abc','PNG')
    # Display image.
    disp.image(image)
    disp.display()
while True: 
  time.sleep(1) 
  showTime()
