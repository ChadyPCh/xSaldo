import os
import threading

def GSB_Toushi():
  os.system("python3 GSB_Toushi.py")
def Soushiro():
  os.system("python3 Soushiro.py")

t1= threading.Thread(target=GSB_Toushi)
t2= threading.Thread(target=Soushiro)

t1.start()
t2.start()
