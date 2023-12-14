import pyperclip
import time

# init variables
copied_text = ''
extend = "https://vxtwitter."
link = ''

# make main function
def on_clipboard_change():
    global copied_text
    global link
    new_text = pyperclip.paste()
    if new_text.startswith("https://x.com"):
        link = f"{extend}{new_text[10:]}"
    if new_text.startswith("https://twitter.com"):
        link = f"{extend}{new_text[16:]}"
    else:
        pass

    if new_text.startswith("https://x.com") or new_text.startswith("https://twitter.com"):
        copied_text = new_text
        print(f"Text in clipboard: {copied_text}")

        # copy output text to clip
        print(f"Output: {link}")
        pyperclip.copy(link)

# one time check
on_clipboard_change()

# wait
while True:
    current_text = pyperclip.paste()
    if current_text != copied_text and current_text != link:
        on_clipboard_change()
    time.sleep(1)
