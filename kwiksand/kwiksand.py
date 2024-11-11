import time
import shutil

def kwik(text, delay=0.04):
    global txt
    txt = []
    if len(text) > shutil.get_terminal_size().columns:
        print(f"ERR: Text too long! Your text is {len(text)} characters while your output can only print {shutil.get_terminal_sie().columns} characters.")
    else:
        txt.clear()
        for l in text:
            txt.append(l)
        for i in range(len(txt)):
            print(*txt[0:i], sep="", end='\r')
            time.sleep(delay)
        print(*txt[0:len(txt)], sep="")
