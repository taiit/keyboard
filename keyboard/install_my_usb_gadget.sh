#!/bin/bash

echo Install to /usr/lib/systemd/system/myusbgadget.service
sudo cp myusbgadget.service /usr/lib/systemd/system/

echo Install to /usr/local/bin/_enable_usb_hid.sh
sudo cp _enable_usb_hid.sh /usr/local/bin/

sudo systemctl start myusbgadget.service
sudo systemctl enable myusbgadget.service

# enable usbSerial console tty
sudo systemctl enable getty@ttyGS0.service
