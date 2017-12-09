# IOT-Pi3-Alexa-Automation

Youtube tutorial https://www.youtube.com/watch?v=uS5dTx8vjq4

Use Raspberry Pi 3 as home automation device with Alexa. This project allows you to control multiple devices connected to Raspberry Pi 3 with voice command. You are able to control GPIO pins thus control GPIO connected devices.

Ported from original repos for python 3
https://github.com/toddmedema/echo
https://github.com/xtacocorex/CHIP_IO 

## Instructions:

1. Download "RASPBIAN STRETCH WITH DESKTOP" and unzip "2017-04-10-raspbian-jessie.zip"
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

1. (Optional) download and install VNC client on youe pc https://www.realvnc.com/download/vnc/windows/. Connect VNC to Respberry Pi3 using IP address. Login with user name "pi" and password "raspberry". You should see Pi3 desktop.

    ![alt text](https://raw.githubusercontent.com/nassiramalik/IOT-Pi3-Alexa-Automation/master/images/pi3vnc.png)
1. Launch Pi ssh session with putty or localy through VNC and type following two commands Pi command prompt to update it. "sudo apt-get update" and "sudo apt-get upgrade" (This will take a while)
1. Download this github project as zip file with following command
  "wget https://github.com/nassiramalik/IOT-Pi3-Alexa-Automation/archive/master.zip"
1. Unzip downloaded zip file with "unzip master.zip" command and type "cd IOT-Pi3-Alexa-Automation-master" command after unzip completes
1. (Optional) Entery "sudo pip install virtualenv" command to install virtualenv on Pi
1. (Optional) Enter "virtualenv ipaa-env" command to create virtual environment for your project
1. (Optional) Enter ". ipaa-env/bin/activate" command to activate your project's virtualen vironment
1. Enter "sudo python3 RPi_name_port_gpio.py" command to run Pi IOT program
1. Give voice command to Alex to discover devices "Alexa discover devices" it will search your network and discover your Raspberry Pi 3 as an IOT device.
1. Give a voice command to Alexa "Turn on the office" you should hear a relay clicking sound and led turn on
1. Give a voice command to Alexa "Turn off the office" you should hear a relay clicking sound and led should turn off
