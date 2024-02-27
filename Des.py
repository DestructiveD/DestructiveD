import random
import os
import sys
import time
import re
cmds = ["exit","clear","ifconfig","echo","help"]
while True:
  cmd input("% ")
  if cmd == "exit":
    sys.exit
  elif cmd == "clear":
    os.system("clear")
  elif cmd == "ifconfig":
    os.system("ifconfig")
  elif cmd[:4] == "echo":
    print(cmd[5:])
  elif cmd == "help":
    for i in cmds:
      print(i)
  else:
    if len(cmd.strip()) != 0:
      print(cmd,"is not a valid command.")
      
