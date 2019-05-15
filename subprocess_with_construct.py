import subprocess

with subprocess.Popen("python", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
    stdout, stderr = proc.communicate("print(2)\nprint('Hello sent from script as input')".encode())
    print("Out " + stdout.decode())
    print("Error " + stderr.decode())
