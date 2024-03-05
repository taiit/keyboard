#!/bin/bash
export APT_GET="sudo apt-get install -y"

echo "Run update"
sudo apt-get update

echo "Install common software"
$APT_GET net-tools vim

echo "Install linux kernel build toolchain"

$APT_GET git bc bison flex libssl-dev make libncurses-dev

