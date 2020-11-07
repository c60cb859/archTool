#!/bin/bash

# Home bin
mkdir -p /home/$USER/bin

# Arch Tool
rm /home/$USER/.config/bin/arch
ln -s /home/$USER/.config/archTool/arch.py /home/$USER/bin/arch
