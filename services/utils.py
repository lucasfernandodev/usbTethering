import subprocess

def runCommand(command):
  parse = command.split(" ");
  process = subprocess.run(parse, capture_output=True, text=True);
  return process.stdout;