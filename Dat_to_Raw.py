#Python code to convert .dat to raw file

import os
lowRes= 'stagbeetle208x208x123.dat'
highRes = 'stagbeetle832x832x494.dat'
i = 0

# for lowRes
fp = open('Beatle208','ab')
with open(lowRes, "rb") as f:
    byte = f.read(1)
    while byte:
        if (counter >= 6): 
           fp.write(byte)
        counter = counter + 1
        byte = f.read(1)        
fp.close()

# for HighRes
i = 0
fp = open('Beatle832','ab')
with open(highRes, "rb") as f:
    byte = f.read(1)
    while byte:
        if (counter >= 6): 
           fp.write(byte)
        counter = counter + 1
        byte = f.read(1)        
fp.close()