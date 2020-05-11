import time
import math
from media import *

def movement(jerry,cat, dog):
    lightBlue = makeColor(213, 237, 245)
    pict = makeEmptyPicture(500,500,lightBlue)
    frameList = []
    count = 0 
    for x in range(-425,300,10):
        canvas = duplicatePicture(pict)
        x1 = 150 + int(100*math.sin(x))
        y1 = 230 + int(100*math.cos(x))
        copyInto(jerry,canvas,x1,y1) 
        time.sleep(1)
        frameList.append(canvas)
        
    for x in range(-425,300,10):
        x2 = 260 + int(100*math.sin(x))
        y2 = 200 + int(100*math.cos(x))
        copyInto(cat,canvas,x2,y2) 
        frameList.append(canvas)
        
    for x in range(-425,300,10):
        canvas = duplicatePicture(pict)
        copyIntoWithCutoff(dog, canvas,x,count)
        count = count+2
        frameList.append(canvas)
        
    show(frameList) 


jerry = makePicture('jerry copy.png')
cat = makePicture('cat.png')
dog = makePicture('dog.png')
movement(jerry,cat,dog)


def chromakey(source,bg):
  # source should have something in front of blue, bg is the new background 
  newPicture = duplicatePicture(source)  
  for x in range(0,source.getWidth()): 
    for y in range(0,source.getHeight()): 
      p = getPixel(source,x,y) 
      # definition of blue: If the redness + greenness < blueness 
      if (getRed(p) + getGreen(p) < getBlue(p)): 
      #Then, grab the color at the same spot from the new background 
        setColor(getPixel(newPicture, x, y),getColor(getPixel(bg,x,y))) 
  return newPicture

