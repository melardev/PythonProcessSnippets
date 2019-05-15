import subprocess

cat_process = subprocess.Popen(["cat", "../db/sqlite.py"], stdout=subprocess.PIPE)
grep_process = subprocess.Popen(["grep", "-in", "insert"], stdin=cat_process.stdout, stdout=subprocess.PIPE)
output = grep_process.communicate()[0]
cat_process.stdout.close()
print(output.decode())
