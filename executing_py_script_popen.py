from subprocess import Popen

print('Inside executing py script popen')
for i in range(2):
    # We must call communicate to wait the script to finish
    # otherwise it creates the processes but since this process exits, the child processes are killed automatically
    # Or another solution si to create a completely detached process using shell=True argument(default is False, which
    # means creates a subprocess)
    out, err = Popen(['python', './execute_me.py', str(i)]).communicate()
