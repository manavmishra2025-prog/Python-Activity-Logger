import platform
import time
import logging

window_log = ""

logging.basicConfig(filename=(window_log + "winlogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def get_active_window_title():
    os_name = platform.system()
    if os_name == "Windows":
        import win32gui
        window = win32gui.GetForegroundWindow()
        return win32gui.GetWindowText(window)
    elif os_name == "Darwin":
        return "macOS active window detection is running..."
    elif os_name == "Linux":
        return "Linux active window detection is running..."
    else:
        return "Unknown OS"

last_title = None
while True:
    current_title = get_active_window_title()
    if current_title and current_title != last_title:
        logging.info("Window switched to: {0}".format(current_title))
        last_title = current_title
    time.sleep(1)
