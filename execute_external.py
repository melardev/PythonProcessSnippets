import os
import subprocess
import sys
from subprocess import call
import shlex

return_code = call(["ls", "-l"])

sys.stdout.write("os.system")
os.system("some_command with args")

sys.stdout.write("os.popen")
stream = os.popen("ls -l /")

# instead of
sys.stdout.write(os.popen("echo Hello World").read())

os.spawnlp(os.P_WAIT, "ls", "-l", "/")  # executes in new process
os.execlp("ls", "-l")  # executes in process that replaces this one

sys.stdout.write(subprocess.Popen("echo Hello World", shell=True, stdout=subprocess.PIPE).stdout.read())
return_code = subprocess.call("echo Hello World", shell=True)

# Method 5 for 3.5 and above
subprocess.run

p = subprocess.Popen('ls -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p = subprocess.Popen(['ls', '-l'], shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
p.wait()

for line in p.stdout.readlines():
    sys.stdout.write(line, )
retvl = p.wait()

subprocess.call("exit 1", shell=True)

cmd = shlex.split("ls -l /")
p = subprocess.Popen(cmd)

import difflib
from subprocess import Popen, PIPE

files = [(str(i).rjust(4, '0') + '.txt') for i in range(1, 11)]
output_lines = []

for f1 in range(len(files) - 1):
    f2 = f1 + 1
    p = Popen(['diff', files[f1], files[f1 + 1]], stdout=PIPE)
    lines = p.stdout.readlines()[1::2]
    for line in lines:
        output_lines.append(line)

guess = ''
# Each of these sections look breakable into fours
for i in range(0, len(output_lines), 2):
    sys.stdout.write(str(i) + "...")
    original = output_lines[i][2:]
    replaced = output_lines[i + 1][2:]
    sys.stdout.write(original)
    sys.stdout.write(replaced)
    diff = ''
    for x in difflib.ndiff(original[2:], replaced[2:]):
        if x.startswith('+'):
            diff += x[2:]
    sys.stdout.write(diff.replace(' ', ''))
    guess += diff.replace(' ', '')

sys.stdout.write("This your flag?: " + guess)
