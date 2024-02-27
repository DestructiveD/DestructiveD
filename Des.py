import random
import os
import sys
import time
import re
while True:
  cmd input("% ")
  if cmd == "exit":
    sys.exit
  else:
    if len(cmd.strip()) != 0:
      print(cmd,"is not a valid command.")
      
