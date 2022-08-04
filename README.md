# THE PROBLEM:
![ezgif-5-86271457e6](https://user-images.githubusercontent.com/33498670/167284292-2fe06593-0e47-4c7e-8086-8abd2237466c.gif)

Not only its slow, but when mouse cursor happens to be in the center of the screen, it selects the wrong language for you!

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# THE SOLUTION (get rid of the pop up):

Install ["issw"](https://github.com/vovkasm/input-source-switcher) a small utility for macos to switch input sources from a command line.
------------

    git clone git@github.com:vovkasm/input-source-switcher.git
    cd input-source-switcher
    mkdir build && cd build
    cmake ..
    make
    make install

Create fn-lang-switcher.py file in ~/.
------------

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
"<179>" is key code for "fn".

Set this to "Do Nothing"
------------
![ezgif-5-aeb126ae5e](https://user-images.githubusercontent.com/33498670/167285047-18f7a509-b56d-4f1f-896a-963c034947dc.jpeg)

Then run this script on log in (python3 should be installed)
------------

Copy file `com.your_user_name.osx.fn-lang-switcher.plist` into `~/Library/LaunchAgents/`. Change __your_user_name__ in a filename to your real username. Do the same thing inside the plist-file.
Also change __path_to_python_file__ inside the plist-file to the folder where you put the `fn-lang-switcher.py` file.

Run in terminal:

    launchctl load ~/Library/LaunchAgents/com.your_real_username.osx.fn-lang-switcher.plist


More information you'll find [here](https://stackoverflow.com/a/9523030/16259768).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
# RESULT:
You can toggle input source with "fn" button, but without showing the pop up!

