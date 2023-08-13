from time import sleep as wait
import keyboard

try: exec("toggle_key")
except: toggle_key = "home"
try: exec("delay")
except: delay = 0.02
try: exec("macro_buttons")
except: macro_buttons = macro_buttons = ["w", "a", "s", "d"]

event_enabled = True

def on_press(event):
    global event_enabled
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
        print("Macro aktif:", event_enabled, " ", end="\r")
    elif event.name == '/':
        event_enabled = False


keyboard.on_press(on_press)

try:
    while True:
        if keyboard.is_pressed('ctrl') and keyboard.is_pressed('end'): break
        wait(0.2)
except KeyboardInterrupt:
    pass
