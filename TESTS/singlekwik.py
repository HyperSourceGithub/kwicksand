import os 
import func
import time

thing = "really long text to test the kwik system. the kwik system effectively creates a list with items and then prints them one by one."

# main loop
os.system('clear')
print("Welcome to the kwiksand environment!")
func.kwiklist()
time.sleep(3)
func.kwik(thing)
func.kwiklist()
func.kwiklist_str()