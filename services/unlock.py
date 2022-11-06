"""
Reference ===
  https://stackoverflow.com/questions/35275828/is-there-a-way-to-check-if-android-device-screen-is-locked-via-adb
"""


import os
from utils import runCommand
from dotenv import load_dotenv

load_dotenv()

def turnOnPhone():
  command = 'adb shell input keyevent 26';
  stdout = runCommand(command);
  return stdout;


def screenState():
  command = 'adb shell dumpsys nfc';
  stdout = runCommand(command);
  screenInfo = list(filter(lambda k: 'mScreenState' in k, stdout.split("\n")))


  # ON_UNLOCKED / ON_LOCKED / OFF
  screenStateValue = screenInfo[0].split("=")[1];
  return screenStateValue 



def unlockScreen():
  secret = os.getenv('PHONE_PASSWORD');
  currentState = screenState();
  print(secret)
  if(currentState == 'OFF'):
    turnOnPhone();
    command = f'adb shell input text {secret}';

    commandEnter = 'adb shell input keyevent 66';
    runCommand(command);
    stdout = runCommand(commandEnter);
    return stdout



  elif(currentState == 'ON_LOCKED'):
    command = f'adb shell input text {secret}';
  
    commandEnter = 'adb shell input keyevent 66';
    runCommand(command);
    stdout = runCommand(commandEnter);
    return stdout

  else:
    return 'Your Phone is Unlock'

print(unlockScreen())