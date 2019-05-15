import subprocess

proc = subprocess.Popen('ls . && inexistent_command', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, error_output = proc.communicate()

print(output.decode('utf-8'))

print('Error output')
print(error_output.decode('utf-8'))
