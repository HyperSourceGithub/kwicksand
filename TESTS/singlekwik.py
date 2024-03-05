import os 
import func
import time

thing = "really long text to test the kwik system. the kwik system effectively creates a list with items and then prints them one by one."

# main loop
os.system('clear')
print("Welcome to the kwiksand environment!")
print("This is a test of the kwik system.")

for i in range(3):
    print(f"Resetting in {3-i}...")
    time.sleep(1)
    func.delete_lines(1)
print("Clearing lines...")
time.sleep(1)
func.delete_lines(3)
time.sleep(1)

func.kwik(f"[1] {thing}")
time.sleep(1)
os.system('clear')

func.syskwik(f"[2] {thing}")
time.sleep(1)
os.system('clear')

func.testkwik(f"[3] {thing}")
time.sleep(1)
os.system('clear')

func.kwiklist()
func.kwiklist_str()
