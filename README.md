# user-space-keylogger

A simple Python script designed to log keystrokes within the user's session on Linux systems without requiring administrative privileges. This project is intended for educational purposes only, to understand how keyloggers work in a limited context.

## Installation

1. **Clone the Repository:**
   ```sh
   git clone <your-github-repo-url>
   cd user-space-keylogger


2. Install Dependencies:
    ```sh
    pip3 install python-xlib pynput
    ```

Usage
X11 Event Capture
```
 python3 x11_keylogger.py
```

This script uses X11 events to capture key presses. It will log keys pressed in any window within your user session.


Window-Focused Key Capture
```
python3 window_keylogger.py
```

  - This script will only log keys pressed in the terminal or window where the script is running.
