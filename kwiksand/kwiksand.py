import time
import shutil

def kwik(text, delay=0.04):
    global txt
    txt = []
    if len(text) > shutil.get_terminal_size().columns:
        print("ERR: Text too long!")
    else:
        txt.clear()
        for l in text:
            txt.append(l)
        for i in range(len(txt)):
            print(*txt[0:i], sep="", end='\r')
            time.sleep(delay)
        print(*txt[0:len(txt)], sep="")
