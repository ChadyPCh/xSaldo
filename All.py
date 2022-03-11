import os
import threading

def GSB_Toushi():
  os.system("python3 GSB_Toushi.py")

t1= threading.Thread(target=GSB_Toushi)

t1.start()
