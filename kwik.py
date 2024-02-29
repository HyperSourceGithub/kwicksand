import time
import os

txt = [] # define a list for the text

def kwik(text):
    txt.clear()
    for l in text:
        txt.append(l)
    for i in range(len(txt)):
        print(*txt[0:i], sep="", end='\r')
        time.sleep(0.8)
    print(*txt[0:len(txt)], sep="")

# main loop
os.system('clear')
print("Welcome to the kwiksand environment!")
while True:
    chosen_print = input("Please enter some text to print: ")
    kwik(chosen_print)