#!/usr/bin/env python3
import subprocess
from pynput import keyboard

def on_press(key):
    key_str = '{0}'.format(key)
    if (key_str == '<179>'):
        result = subprocess.Popen(['/usr/local/bin/issw', '-l'], stdout=subprocess.PIPE)
        output, _ = result.communicate()
        layouts = output.decode('utf-8').split('\n')
        layouts = [str for str in layouts if 'com.apple.keylayout' in str]
        result = subprocess.Popen('/usr/local/bin/issw', stdout=subprocess.PIPE)
        output, _ = result.communicate()
        next_index = (layouts.index(output.decode('utf-8').strip()) + 1) % len(layouts)
        subprocess.run(['/usr/local/bin/issw', layouts[next_index]], stdout=subprocess.DEVNULL)

with keyboard.Listener(on_press=on_press, on_release=None) as listener:
    listener.join()
