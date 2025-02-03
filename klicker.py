import time
import threading
from pynput.mouse import Button, Controller
from pynput.kyeboard import Listener,Keycode

delay = 0.001
button = Button.left
start_stop_key = KeyCode(char="s")
exit_key =Keycode(char="e")

class ClickMouse(threading.Thread):
    def __init__( self, delay, button ):
        super().__init__()
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
                mouse.click(self.button)
                time.sleep(self.delay)

mouse = Contraller()
click_thread = ClickMouse(delay, button)
click_thread.start()
            
