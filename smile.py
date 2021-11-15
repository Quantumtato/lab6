import time
import LED8x8

dataPin, latchPin, clockPin = 16, 20, 21


pattern = [0b00111100, 0b01000010, 0b10100101, 0b10000001, 
0b10100101, 0b10011001, 0b01000010, 0b00111100]
led8x8 = LED8x8.led8x8(dataPin, latchPin, clockPin)

led8x8.writepattern(pattern)

