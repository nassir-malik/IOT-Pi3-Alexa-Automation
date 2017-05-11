# import serial
#
# ser = serial.Serial('/dev/ttyUSB1',115200)
# s = [0,1]
# while True:
# 	read_serial=ser.readline()
# 	s[0] = str(int (ser.readline(),16))
# 	print(s[0])
# 	print(read_serial)


import serial
ser = serial.Serial('/dev/ttyUSB1', 115200, timeout=1)

ser.write('{"name":"led","value":"2"}')

try:
    while 1:
        response = ser.readline()
        print(response)
except KeyboardInterrupt:
    ser.close()

    # import serial
    #
    # locations = ['/dev/ttyACM0', '/dev/ttyACM1', '/dev/ttyACM2', '/dev/ttyACM3', '/dev/ttyACM4', '/dev/ttyACM5',
    #              '/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyUSB2', '/dev/ttyUSB3', '/dev/ttyUSB4', '/dev/ttyUSB5',
    #              '/dev/ttyUSB6', '/dev/ttyUSB7', '/dev/ttyUSB8', '/dev/ttyUSB9', '/dev/ttyUSB10', 'com2', 'com3',
    #              'com4', 'com5', 'com6', 'com7', 'com8', 'com9', 'com10', 'com11', 'com12', 'com13', 'com14', 'com15',
    #              'com16', 'com17', 'com18', 'com19', 'com20', 'com21', 'com1', 'end']
    #
    # for device in locations:
    #     try:
    #         print("Trying...", device)
    #         serialport = serial.Serial(device, 9600, timeout=0)
    #         break
    #     except:
    #         # print "Failed to connect on",device
    #         if device == 'end':
    #             print("Unable to find Serial Port, Please plug in cable or check cable connections.")
    #            exit()