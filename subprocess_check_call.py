import subprocess

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
