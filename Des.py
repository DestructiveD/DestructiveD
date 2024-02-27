import random
import os
import sys
import time
import re
cmds = ["exit","clear","ifconfig","echo","help"]
letterGenerate = random.randint(11111111,99999999)
letterGenerate = str(letterGenerate)
letterGenerate = letterGenerate.replace("1","A").replace("2","B").replace("3","C").replace("4","D").replace("5","E").replace("6","F").replace("7","G").replace("8","H").replace("9","I")
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
  elif cmd[:8] == "generate":
    if cmd[9:] == "letter":
      print(letterGenerate)
  else:
    if len(cmd.strip()) != 0:
      print(cmd,"is not a valid command.")
      
