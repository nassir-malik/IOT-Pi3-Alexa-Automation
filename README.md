# IOT-Pi3-Alexa-Automation
Use Raspberry Pi 3 as home automation device with Alexa. This project will allows you to control multiple devices connected to Raspberry Pi 3 with voice command. You area able to control GPIO pins thus control GPIO connected devices.

Ported from original repos for python 3
https://github.com/toddmedema/echo
https://github.com/xtacocorex/CHIP_IO 

## Instructions:

1. Download "RASPBIAN JESSIE WITH PIXEL" and unzip "2017-04-10-raspbian-jessie.zip"
  https://www.raspberrypi.org/downloads/raspbian/

1. Download "win32diskimager-1.0.0-install.exe" program from following URL
  https://sourceforge.net/projects/win32diskimager/files/latest/download

1. Install "win32diskimager-1.0.0-install.exe"

1. Connect mini-sd card to a computer. In windows explorer right click your sd card drive letter and click on format menue.
  In format window select "FAT" in "File System" list file and click start.
  
  ![alt text](https://raw.githubusercontent.com/nassiramalik/IOT-Pi3-Alexa-Automation/master/images/formatsdcard.jpg)
  
1. Launch "win32diskimager" program. Select image file "2017-04-10-raspbian-jessie.img" and your sd card drive letter and click "Write"
  (Wait for program to finish writing REAPBIAN image to the sd card)
      
    ![alt text](https://raw.githubusercontent.com/nassiramalik/IOT-Pi3-Alexa-Automation/master/images/win32diskimager.jpg)

1. Once image wrting is completed, open windows explorer and click on sd card driver letter and create a "ssh" file without any extenssion.

1. Insert the sd card into Raspberry Pi 3 and boot

1. 
