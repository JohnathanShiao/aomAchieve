import time
import threading
from pynput.mouse import Button, Controller as MController
from pynput.keyboard import Listener,Key, KeyCode, Controller as KController


delay = 0.5
button = Button.left
start_stop_key = KeyCode(char='[')
exit_key = KeyCode(char=']')


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.position = (1000,900) #create game
                mouse.click(self.button)
                time.sleep(1)
                keyboard.press('a')     #name game
                keyboard.release('a')
                mouse.position = (700,625) #hit yes
                mouse.click(self.button)
                time.sleep(1)
                mouse.position = (400,180)  #click empty
                mouse.click(self.button)
                time.sleep(1)
                mouse.position = (400,200)  #click standard ai
                mouse.click(self.button)
                time.sleep(1)
                mouse.position = (1200,550)    #switch gamemode
                mouse.click(self.button)
                time.sleep(1)
                mouse.position = (1200,650)    #choose gamemode
                mouse.click(self.button)
                time.sleep(1)
                mouse.position = (1025,140)
                mouse.click(self.button)
                time.sleep(15)
                keyboard.press(Key.f10) #open menu
                keyboard.release(Key.f10)
                time.sleep(1)
                mouse.position = (800,350) #choose resign
                mouse.click(self.button)
                time.sleep(1)
                mouse.position = (700,450) #hit yes
                mouse.click(self.button)
                time.sleep(1)
                mouse.position = (800,475)
                mouse.click(self.button)
                time.sleep(1)
                keyboard.press(Key.f10)
                keyboard.release(Key.f10)
                time.sleep(1)
                mouse.position = (800,350)
                mouse.click(self.button)
                time.sleep(2)
            time.sleep(1)
            
mouse = MController()
keyboard = KController()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
