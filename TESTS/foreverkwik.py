import os
from func import kwik

# main loop
os.system('clear')
print("Welcome to the kwiksand environment!")
while True:
    chosen_print = input("Please enter some text to print: ")
    kwik(chosen_print)