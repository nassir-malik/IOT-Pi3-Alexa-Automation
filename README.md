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

1. Connect mini-sd card to a computer. In windows explorer right click your sd card drive letter and click on format menu.
  In format window select "FAT" in "File System" list and click start. Wait for the task to complete.
  
    ![alt text](https://raw.githubusercontent.com/nassiramalik/IOT-Pi3-Alexa-Automation/master/images/formatsdcard.jpg)
  
1. Launch "win32diskimager" program. Select image file "2017-04-10-raspbian-jessie.img" and your sd card drive letter and click "Write"
  (Wait for program to finish writing REAPBIAN image to the sd card)
      
    ![alt text](https://raw.githubusercontent.com/nassiramalik/IOT-Pi3-Alexa-Automation/master/images/win32diskimager.jpg)

1. Once image writing is completed, Copy "ssh" (ssh file is empty) and "wpa_supplicant.conf" files to root of the sd card. Open "wpa_supplicant.conf" in text editor and update ssid (wi-fi name) & password.

1. Insert the sd card into Raspberry Pi 3 and boot and wit for 10 seconds

1. In windows go to run & type "cmd" and type arp -a in command prompt. Look for "Physical Address" that starts with b8-27\* & note the Internet Address. This is your Raspberry Pi3 Wi-fi IP address on your network.
  
    ![alt text](https://raw.githubusercontent.com/nassiramalik/IOT-Pi3-Alexa-Automation/master/images/pi3ipaddress.jpg)
  
1. Download "Putty.exe" from following URL https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html

1. Run "Putty.exe" and type IP address in host name field and click start button & click yes to popup. On putty command line type in "pi" for "Login as:" & enter. For password enter "raspberry" and   hit enter. You should see "pi@raspberrypi:~ $" prompt.

    ![alt text](https://raw.githubusercontent.com/nassiramalik/IOT-Pi3-Alexa-Automation/master/images/puttypi3prompt.png)

1. Type "sudo raspi-config" and go to "Interfacing Options" and enable VNC. Reboot pi3 by typing this command "sudo reboot". You will loose ssh connection.

1. Download and install VNC client on youe pc https://www.realvnc.com/download/vnc/windows/. Connect VNC to Respberry Pi3 using IP address. Login with user name "pi" and password "raspberry". You should see Pi3 desktop.

    ![alt text](https://raw.githubusercontent.com/nassiramalik/IOT-Pi3-Alexa-Automation/master/images/pi3vnc.png)
1. sudo apt-get update sudo apt-get upgrade
1. Download github zip file with following 
  wget https://github.com/nassiramalik/IOT-Pi3-Alexa-Automation/archive/master.zip
1. Unzip downloaded zip file "unzip master.zip" and cd to "IOT-Pi3-Alexa-Automation-master" folder
