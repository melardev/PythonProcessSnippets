import subprocess

p = subprocess.Popen('ping localhost', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
while True:
    line = p.stdout.readline()
    print(line.decode('utf-8'))
    if line == ''.encode('utf-8') and p.poll() == 0:
        break

