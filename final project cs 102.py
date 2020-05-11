import time
import math
from media import *

def movingText():
#specify the strings in opening credits
#store strings in a list
  list = [""]*4    #size of list
  list[0] = "Tom, Jerry, and Spike"
  list[1] = "Code by Linh, Emma, and Ryoko"
  list[2] = "Sound by Emma"
  list[3] = "Sound by Emma"
  
  
  # create an empty picture for exposition
  h = 400
  w = 400
  # make a background color
  lightBlue = makeColor(213, 237, 245)
  pict = makeEmptyPicture(w, h, lightBlue)
  show(pict)
  
  #make a pretty font
  myFont = makeStyle(serif ,bold, 18)
  #make a font color
  fontColor = makeColor(24, 33, 133)
  
  #scroll the text   
  for scroll in range(1, 340, 20):
     #starting credits position for each scrolling pass
     y = 15 + scroll
     #draw the text in each list item 
     for credits in range(0, len(list)):
       #centering text - not very accurate
       #get the length of the string and divide in half
       # multiply by 1/2 font size, which is 18
       length = len(list[credits]) / 2 * 9
       addTextWithStyle(pict, w / 2 - length, y ,list[credits], myFont, fontColor)
       #time.sleep(.1)  #delay for 1/2 second
       #next credit drawn 20 units down in y
       y += 20
       repaint(pict)
     time.sleep(0.4)   #delay for 2 seconds before erasing text
     setAllPixelsToAColor(pict, lightBlue)
  
  #final erase of text
  setAllPixelsToAColor(pict, lightBlue)
  repaint(pict)


def movement(jerry,cat,dog,a,b):
    lightBlue = makeColor(213, 237, 245)
    pict = makeEmptyPicture(1000,1000,lightBlue)
    
    for y in range(50):
        canvas = duplicatePicture(pict)
        x1 = a + int(150*math.sin(y+2))
        y1 = b + int(150*math.cos(y+2))
        copyInto(jerry,canvas,x1,y1) 
        time.sleep(0.3)
  
        x2 = a + int(150*math.sin(y+1))
        y2 = b + int(150*math.cos(y+1))
        copyInto(cat,canvas,x2,y2) 
        time.sleep(0.3)
            
        x3 = a + int(150*math.sin(y))
        y3 = b + int(150*math.cos(y))
        copyInto(dog,canvas,x3,y3) 
        time.sleep(0.3)
        show(canvas)
jerry = makePicture('jerry copy.png')
cat = makePicture('cat.png')
dog = makePicture('dog.png')
movement(jerry,cat,dog, 500, 500)


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