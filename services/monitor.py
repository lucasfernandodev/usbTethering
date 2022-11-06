from .unlockPhone import unlockScreenPhone, getScreenState;
from .usbTethering import getUsbTetheringState, setUsbTethering;

import os.path
import pyudev;
import os
import time
from dotenv import load_dotenv;


load_dotenv()

def MonitorUsbPhone():

  # Tenta iniciar o tethering 
  unlockScreenPhone();
  if(getScreenState() == 'ON_UNLOCKED'):
    usbTetheringState = getUsbTetheringState();
  if(usbTetheringState != 'online'):
    setUsbTethering()

  # Inicia o monitor
  context = pyudev.Context()
  monitor = pyudev.Monitor.from_netlink(context)
  monitor.filter_by(subsystem='usb')  # Remove this line to listen for all devices.
  monitor.start();

  # Pega os novos dispositivos conectados
  for device in iter(monitor.poll, None):
    currentDevice = device.get('ID_SERIAL_SHORT');

    # Device is connected!
    if(currentDevice == os.getenv('PHONE_SERIAL')):
      time.sleep(2);
      unlockScreenPhone();

      if(getScreenState() == 'ON_UNLOCKED'):
        usbTetheringState = getUsbTetheringState();

        if(usbTetheringState != 'online'):
          setUsbTethering()

