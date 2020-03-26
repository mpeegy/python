import subprocess
 
args = ["ping", "ya.ru"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
 
data = process.communicate()
for line in data:
    print(line)


input()
