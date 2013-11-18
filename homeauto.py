# homeauto.py the main file to run the raspberry pi automation system
# current dummy program only outputs text for the action taken
# displays device state as text only
# Lets think what happens when u switch on the system
# (1) get all connected devices and their types
# (2) get the state of all connected devices
# (3) get the current system time
# (4) check if any predefined routine is to be run at this time
# (4a) if predef routine file exists
# (4b) if there is any routine in predef file
# (5) if no current predef routine, wait for user input

import datetime
predef_prog=False
current_connected_device=[]
current_device_state={}
current_system_time=datetime.datetime.now()
print "Hello this is the RPi Home Automation program"
# print current_system_time
try:
   with open('homeprogram.csv'):
       predef_prog=True
except IOError:
    predef_prog=False

print "The predef program was "
if predef_prog==True:
   print "Found"
else:
   print "Not found"
