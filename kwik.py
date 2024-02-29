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

# tests
print("KWIKSAND TEST")
kwik("Hello World!")
kwik("I am Bob!")
kwik("This is a text engine.")