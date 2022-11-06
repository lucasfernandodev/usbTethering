#!/usr/bin/env python

import functools
import os.path
import pyudev
import subprocess
import time

def main():
    phoneSerialId = 'df6ab456';

    BASE_PATH = os.path.abspath(os.path.dirname(__file__))
    path = functools.partial(os.path.join, BASE_PATH)
    call = lambda x, *args: subprocess.call([path(x)] + list(args))

    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')  # Remove this line to listen for all devices.
    monitor.start()

 # Verifica se existe uma interface usb0
    def getUSBtetheringStatus():

      execCommand = subprocess.run('ip route list'.split(" "), capture_output=True, text=True);
      
      if 'usb0' in execCommand.stdout:
        print("O USBtethering está ativado.")
        return 'active'


    # Ativa o thering via adb
    def setUSBtethering():
      commandOpenMenu = 'adb shell "am start -n com.android.settings/.TetherSettings;'
      commandActiveOption = 'adb shell input tap 282 430;'
      commandCloseMessageErrorSdCard = 'adb shell input tap 913 1016"'

      isTethering = getUSBtetheringStatus();
      print(isTethering)
      if(isTethering != 'active'):
        subprocess.run(commandOpenMenu.split(" "));
        subprocess.run(commandActiveOption.split(" "));
        subprocess.run(commandCloseMessageErrorSdCard.split(" "));
        getUSBtetheringStatus();

   

      
    # Encaminha a porta ssh
    def forward():
      forwarding_port = subprocess.run(["adb","forward","tcp:8066", "tcp:8066"])
      print("Forward command => %s" % forwarding_port)








    for device in iter(monitor.poll, None):
      deviceCurrent = device.get('ID_SERIAL_SHORT');
      # I can add more logic here, to run only certain kinds of devices are plugged.
      if(deviceCurrent == phoneSerialId):
        print('connected!')
        time.sleep(2)
        forward()
        setUSBtethering()

if __name__ == '__main__':
    main()