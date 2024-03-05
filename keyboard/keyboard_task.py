#!/usr/bin/python3
import time, os
from evdev import InputDevice, categorize, ecodes

keyboard_dev_name='/dev/input/event1'
hid_command='sudo /home/dev/work/keyboard/hid-gadget-test/hid-gadget-test /dev/hidg0 keyboard'

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())


key_map = {
    'KEY_A': 'a'

}

try:
    time.sleep(5)
    while True:
        try:
            dev = InputDevice(keyboard_dev_name)
            print(dev)
            for event in dev.read_loop():
                #print("{}, {} , {} ".format(type(event), event.type, event))
                if event.type == ecodes.EV_KEY:
                    key_event = categorize(event)
                    key_code = key_map.get(key_event.keycode, None)
                    #import pdb; pdb.set_trace()
                    if key_code:
                        if event.value == 0: # key_up
                            print("Sending key_code: {}".format(key_code))
                            #os.system("echo {} | {}".format(key_code, hid_command)) 
                            # Release keys
                            write_report(NULL_CHAR*8)
                        elif event.value == 2: # key_hold
                            #os.system("echo {} {} | {}".format(key_code, "hold", hid_command)) 
                            # Press a
                            write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
                        elif event.value == 1: # key_down
                            write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
                            pass
                    else:
                        pass
                    print("Unknown: {}".format(key_event))
        except:
            print("Can not open {}, retry after 10s".format(keyboard_dev_name))
            time.sleep(10)
except KeyboardInterrupt:
    print('interrupted!')