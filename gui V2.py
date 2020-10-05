""" Rev V2
    Simulate mouse activity so that site won't log me off.
"""    
import pyautogui as gui
import time
from win10toast import ToastNotifier
toast = ToastNotifier()
print(gui.size())
sx,sy = gui.size()
time.sleep(3)

while True:
    toast.show_toast("ROBOT !","Robot is active.", threaded = False, icon_path= None,duration = 2)
    time.sleep(5)
    gui.click() #Click the open area and press PageUp so that bot clicks match the location of the links.
    gui.press('home') # Same as above
    gui.moveTo(541,142,0.25) # 'Transfer' dropdown
    gui.click()
    time.sleep(2)
    gui.moveTo(541,172,0.25) # 'Transfer' link
    gui.click()
    print('Robot is active...')
    print('Time:\t',time.time())
    time.sleep(60)
    gui.moveTo(942,142,0.25) # 'AEP' dropdown
    gui.click()
    time.sleep(1)
    gui.moveTo(942,162,0.25) # 'AEP' link
    gui.click()
    time.sleep(600)
    
