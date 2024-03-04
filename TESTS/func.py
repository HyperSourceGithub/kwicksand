import time

txt = [] # define a list for the text

def kwik(text):
    txt.clear()
    for l in text:
        txt.append(l)
    for i in range(len(txt)):
        print(*txt[0:i], sep="", end='\r')
        time.sleep(0.08)
    print(*txt[0:len(txt)], sep="")

def kwiklist():
    print(txt)

def kwiklist_str():
    print(*txt, sep="")

