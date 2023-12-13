import pystray
from pystray import MenuItem as item
from PIL import Image
import pyperclip
import time
from threading import Thread
import sys

# Init variables
copied_text = ''
extend = "https://vxtwitter."
link = ''

# Define the main function
def on_clipboard_change(icon, item):
    global copied_text
    global link
    new_text = pyperclip.paste()

    if new_text.startswith("https://x.com") or new_text.startswith("https://twitter.com"):
        link = f"{extend}{new_text[10:]}"
        copied_text = new_text
        print(f"Текст у буфері обміну: {copied_text}")
        print(f"Текст після зміни: {link}")
        pyperclip.copy(link)

        # condition to exit the program
        if new_text == "exit_condition":
            icon.stop()
            sys.exit()

# Create a blank image for the icon
image = Image.new('RGB', (128, 128), color=(255, 255, 255))

# Create menu items
menu = (item('', lambda icon, item: icon.stop()),)
menu = (item('Stop and close', lambda icon, item: sys.exit()),)

# Create the system tray icon
icon = pystray.Icon("name", image, "Title", menu)

# Define the main function to run in a separate thread
def main_thread():
    while True:
        on_clipboard_change(icon, None)
        time.sleep(1)

# Run the main function in a separate thread
Thread(target=main_thread).start()

# Run the system tray icon
icon.run()