# PRODIGY_CS_04
A basic keylogger built with Python to record and log keystrokes locally.

# Simple Keylogger

## Description

This is a basic keylogger that records keyboard inputs and saves them to a log file. The focus is on understanding how input devices interact with applications and how event-driven programming works at a low level.

## Objective

- Create a basic keylogger using Python that records keystrokes.
- Store all captured keystrokes in a local text file.
- Understand event listeners and logging mechanisms.
- Practice ethical implementation in controlled environments.

## Technologies Used

- Python 3.x
- pynput library

## How It Works

The script listens for all keyboard input events using the `pynput` module. When a key is pressed, it captures the event and writes it into a log file (`keylog.txt`). The program runs continuously until the **Esc** key is pressed to stop it safely.

### Install Pynput:

```bash
pip install pynput
```

## How to use

1. Save the Python script as `keylogger.py`.
2. Open a terminal or command prompt.
3. Navigate to the script directory:
   ```bash
   cd path_to_your_file
   ```
4. Run the script:
   ```bash
   python keylogger.py
   ```
5. Press keys on your keyboard.
6. Press **Esc** to stop logging.
7. Open `keylog.txt` to view the captured keystrokes.

## Sample Output

```
2025-05-03 14:35:22,134 - Key pressed: a
2025-05-03 14:35:23,800 - Key pressed: b
2025-05-03 14:35:24,521 - Special key pressed: Key.space
2025-05-03 14:35:25,621 - Key pressed: c
```

## Files

- `keylogger.py` – Main Python script
- `README.md` – Project documentation
- `keylog.txt` – Auto-generated keystroke log file (ignored in Git)

## Note

Unauthorized use of keyloggers is illegal and violates ethical computing standards. Always seek permission before using monitoring software on any system.

---
