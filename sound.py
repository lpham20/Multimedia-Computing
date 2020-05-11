import sys, os
sys.path.append(os.path.dirname(sys.path[0]))
from media import *

def decreaseVolume(sound):
    samples = getSamples(sound)
    for index in range(len(samples)):
        sample = samples[index]
        value = getSampleValue(sample)
        setSampleValue(sample, value * 0.5)
        
s = makeSound("credits.wav")
decreaseVolume(s)
saveSound(s)