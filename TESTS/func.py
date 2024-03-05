import time
import sys

txt = [] # define a list for the text

def delete_lines(n):
    for _ in range(n):
        sys.stdout.write("\x1b[1A")  # cursor up one line
        sys.stdout.write("\x1b[2K")  # delete the last line

def testkwik(text):
    for i in range(len(text)):
        print(text[0:i])
        time.sleep(0.08)
        delete_lines(1)
    print(text)

def kwik(text):
    txt.clear()
    for l in text:
        txt.append(l)
    for i in range(len(txt)):
        print(*txt[0:i], sep="", end='\r')
        time.sleep(0.08)
    print(*txt[0:len(txt)], sep="")

def syskwik(text):
    txt.clear()
    for l in text:
        txt.append(l)
    for i in range(len(txt)):
        print(*txt[0:i], sep="") #, end='\r')
        sys.stdout.write("\x1b[1A")
        sys.stdout.write("\x1b[2K")
        time.sleep(0.08)
    print(*txt[0:len(txt)], sep="")

def kwiklist():
    print(txt)

def kwiklist_str():
    print(*txt, sep="")

