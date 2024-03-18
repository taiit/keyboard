#!/bin/bash
export APT_GET="sudo apt-get install -y"

echo "Run update"
sudo apt-get update

echo "Install common software"
$APT_GET net-tools vim

echo "Install linux kernel build toolchain"

$APT_GET git bc bison flex libssl-dev make libncurses-dev

# Install GUI
#    XOG. sudo apt install xserver-xorg -y
#    XFCE: sudo apt install xfce4 xfce4-terminal -y
#    Display Manage:  sudo apt install lightdm -y
#       Select the display server: sudo systemctl get-default && sudo systemctl set-default graphical.target
#       Select the display manager: sudo dpkg-reconfigure lightdm
#       Select the session manager: sudo update-alternatives --config x-session-manager
#       Select the window manager: sudo update-alternatives --config x-window-manager

#  --> sudo reboot