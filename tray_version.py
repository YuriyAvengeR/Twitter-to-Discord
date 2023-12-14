import pystray
from pystray import MenuItem as item
from PIL import Image
import pyperclip
import time
from threading import Thread

# Init variables
copied_text = ''
extend = "https://vxtwitter."
link = ''
stop_thread = False  # Flag

# Stop thread
def stop_program(icon, item=None):
    global stop_thread
    stop_thread = True
    icon.stop()

# Define the main function
def on_clipboard_change(icon, item):
    global copied_text
    global link
    new_text = pyperclip.paste()

    if new_text.startswith("https://x.com"):
        link = f"{extend}{new_text[10:]}"
    if new_text.startswith("https://twitter.com"):
        link = f"{extend}{new_text[16:]}"
        print(link)
    else:
        pass

    if new_text.startswith("https://x.com") or new_text.startswith("https://twitter.com"):
        copied_text = new_text
        pyperclip.copy(link)

        # condition to exit the program
        if new_text == "exit_condition":
            stop_program(icon)

# Create a blank image for the icon
image = Image.new('RGB', (128, 128), color=(255, 255, 255))

# Create menu items
menu = (
    item('Close', stop_program),
)

# Create the system tray icon
icon = pystray.Icon("Twitter to Discord", image, "Twitter to Discord", menu)

# Define the main function to run in a separate thread
def main_thread():
    while not stop_thread:  # stop thread
        on_clipboard_change(icon, None)
        time.sleep(1)

# Run the main function in a separate thread
thread = Thread(target=main_thread)
thread.start()

# Run the system tray icon
icon.run()
