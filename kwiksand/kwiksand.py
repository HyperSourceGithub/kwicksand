import time
import shutil

def kwik(text, delay=0.04, overprint=False):
    global txt
    txt = []
    if len(text) > shutil.get_terminal_size().columns and overprint == False:
        print(f"ERR: Text too long! Your text is {len(text)} characters while your output can only print {shutil.get_terminal_size().columns} characters.")
        print("To circumvent this, set the \'overprint\' property to True.")
    elif len(text) > shutil.get_terminal_size().columns and overprint == True:
        print(text)
    else:
        txt.clear()
        for l in text:
            txt.append(l)
        for i in range(len(txt)):
            print(*txt[0:i], sep="", end='\r')
            time.sleep(delay)
        print(*txt[0:len(txt)], sep="")
