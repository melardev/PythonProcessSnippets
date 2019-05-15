import subprocess

p = subprocess.Popen('ls . && inexistent_command', shell=True,
                     stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                     close_fds=True)
output = p.stdout.read()
print(output.decode('utf-8'))
