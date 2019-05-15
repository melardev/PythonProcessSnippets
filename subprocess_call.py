import subprocess

# this module is the replacement for os.system, os.spawn, os.popen, os.popen2, etc
exit_code = subprocess.call("whoami")  # execute and wait to finish
print(exit_code)
r = subprocess.call("ls")
subprocess.call(['ls', '-al'])
