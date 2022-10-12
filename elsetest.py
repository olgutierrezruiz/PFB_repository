#!/usr/bin/env python3
import sys
numberx = int(sys.argv[1])
if numberx > 0:
  print('positive')
  if numberx < 50:
    print('numberx < 50')  
    if numberx % 2 == 0:
      print('it is an even number that is smaller than 50')
    else:
      print('odd')    
elif numberx == 0:
  print('equal to 0')
else:
    print('negative')


