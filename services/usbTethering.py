from .utils import runCommand

INTERFACE = 'usb0';

def getUsbTetheringState():
  command = 'ip route list';
  stdout = runCommand(command);
      
  if(INTERFACE in stdout):
    return 'online'
  else:
    return 'offline'


def setUsbTethering():
  commandOpenMenu = 'adb shell "am start -n com.android.settings/.TetherSettings;'
  commandActiveOption = 'adb shell input tap 282 430;';
  
  runCommand(commandOpenMenu)
  runCommand(commandActiveOption);

  usbTetheringState = getUsbTetheringState()
  if(usbTetheringState == 'online'):
    return 'success'
  else:
    return 'error';

def closeMessagingErrorSdCard():
  command = "adb shell input tap 913 1016";
  runCommand(command)
