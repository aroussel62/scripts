#!/usr/bin/python

import broadlink
import time
import sys

device = broadlink.rm(host=("ici votre adresse ip avec les points il faut conserver les guillemets",80), mac=bytearray.fromhex("ici votre adresse mac il faut conserver les guillemets"))

print "Connecting to Broadlink device...."
device.auth()
time.sleep(1)
print "Connected...."

codeName = raw_input("Please Enter Code Name  e.g. tvOff ")
time.sleep(1)
print "When Broadlink white led is lit press the button on your remote within 5 seconds"

device.host
device.enter_learning()
time.sleep(5)
ir_packet = device.check_data()
#convert code to hex
myhex = str(ir_packet).encode('hex'); 

if ir_packet == None:
   print "No button press read - quitting"
   sys.exit()
else:

# record learned hex code to file
   f = open(codeName +".txt",'w')
f.write(myhex)
f.close()

print "Hex code written to file named " + codeName + ".txt"
