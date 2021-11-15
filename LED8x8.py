import time
import Shifter





class led8x8():

  def __init__(self, data, latch, clock):
    self.dataPin, self.latchPin, self.clockPin = data, latch, clock

    self.shifty = Shifter.shifter(self.dataPin, self.latchPin, self.clockPin)

  def writepattern(self,pattern):
    for i in range(len(pattern)):
      writebit = pattern[i]
      writebit = writebit << 8
      
      colbit = 0b0
      for j in range(8):
        if j == i:
         colbit += 0 #redundant, included for legibiligys sake
        else:
          colbit +=1 
        if j != 7:
         colbit = colbit << 1
      #print(bin(colbit))
      writebit = writebit + colbit
      print(bin(writebit))
      
      self.shifty.shiftbyte(writebit)