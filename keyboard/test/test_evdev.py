import evdev
from evdev import InputDevice, categorize, ecodes

devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
for device in devices:
    print(device.path, device.name, device.phys)

#dev = InputDevice('/dev/input/event1')
#print(dev)
#for event in dev.read_loop():
#    if event.type == ecodes.EV_KEY:
#        print(categorize(event))
