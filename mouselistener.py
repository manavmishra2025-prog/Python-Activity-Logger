from pynput.mouse import Listener
import logging
from pynput import mouse

log_dir_mouse = ""

logging.basicConfig(filename=(log_dir_mouse + "mouselogs.txt"), level = logging.DEBUG, format = "%(asctime)s: %(message)s")

def on_move(x, y):
    logging.info("Mouse moved to ({0}, {1})".format(x, y))

def on_click(x, y, button, press):
    logging.info("{0}-click at ({1}, {2})".format(button, x, y))

def on_scroll(x, y, dx, dy):
    logging.info("Mouse scrolled at ({0}, {1})({2}, {3})".format(x, y, dx, dy))

with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mlistener:
    mlistener.join()