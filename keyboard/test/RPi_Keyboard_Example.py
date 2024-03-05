#!/usr/bin/env python3
import time

USB_KEY_NULL = 0
USB_KEY_SHIFT = 32


kbmap = dict()

kbmap['a'] = (USB_KEY_NULL, 4)
kbmap['A'] = (USB_KEY_SHIFT, 4)

def send_chr(input_char) :
    if not input_char in kbmap.keys() :
        print("Unknow input_char: ", input_char)
        return
    # https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-report-descriptor/
    # 1 byte: modifier keys (Control, Shift, Alt, etc.), where each bit corresponds to a key
    # 1 byte: unused/reserved for OEM
    # 6 bytes: pressed key codes
    keymap_dict = kbmap.get(input_char)
    buf = chr(keymap_dict[0]) +  chr(USB_KEY_NULL) + chr(keymap_dict[1]) + chr(USB_KEY_NULL)*5
    send_report(buf)


def send_key_up():
    buf = chr(USB_KEY_NULL) *8
    send_report(buf)

def send_key_shift():
    buf = chr(225) +  chr(USB_KEY_NULL) + chr(USB_KEY_NULL) + chr(USB_KEY_NULL)*5
    send_report(buf)

def send_report(report):
    reprot_data = report.encode()
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(reprot_data)

print("Waiting for 3s")
time.sleep(3) # Sleep for 3 seconds
#cat /proc/bus/input/devices
send_chr('a')
send_key_up()

#send_chr('A')

#send_key_shift()

#send_key_up()

# Press a
#write_report(NULL_CHAR*2 + chr(4) + NULL_CHAR*5)
# Release keys
#write_report(NULL_CHAR*8)

# Press SHIFT + a = A
#write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)

#write_report(chr(32)+ NULL_CHAR*2 + NULL_CHAR*5)
#write_report(NULL_CHAR*2 + chr(4) + NULL_CHAR*5)

# # Press b
# write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
# # Release keys
# write_report(NULL_CHAR*8)
# # Press SHIFT + b = B
# write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)

# # Press SPACE key
# write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)

# # Press c key
# write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)
# # Press d key
# write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5)

# # Press RETURN/ENTER key
# write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)

# # Press e key
# write_report(NULL_CHAR*2+chr(8)+NULL_CHAR*5)
# # Press f key
# write_report(NULL_CHAR*2+chr(9)+NULL_CHAR*5)

