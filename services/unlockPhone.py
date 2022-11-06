import os
from .utils import runCommand
from dotenv import load_dotenv

load_dotenv()

def turnOnPhone():
  command = 'adb shell input keyevent 26';
  stdout = runCommand(command);
  return stdout;


def getScreenState():
  command = 'adb shell dumpsys nfc';
  stdout = runCommand(command);
  screenInfo = list(filter(lambda k: 'mScreenState' in k, stdout.split("\n")))
  screenStateValue = screenInfo[0].split("=")[1];
  return screenStateValue # ON_UNLOCKED / ON_LOCKED / OFF


def unlockScreen():
  password = os.getenv('PHONE_PASSWORD');
  command = f'adb shell input text {password}';
  commandEnter = 'adb shell input keyevent 66';
  runCommand(command);
  stdout = runCommand(commandEnter);
  return stdout;


def unlockScreenPhone():
  
  currentState = getScreenState();

  if(currentState == 'OFF'):
    turnOnPhone();
    unlockScreen()

  elif(currentState == 'ON_LOCKED'):
    unlockScreen()

  else:
    return 'Your Phone is Unlock'
