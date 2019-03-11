from subprocess import Popen, PIPE

p = Popen(["du", "-h"], stdout=PIPE, stderr=PIPE)
out,err = p.communicate()

out = out.decode("utf-8")
out = out.split("\n")

print("The following directories are bigger than 1MB")

for line in out:
	spliterinos = line.split("\t")
	sizePart = spliterinos[0]
	if sizePart.endswith("M"):
		if float(sizePart[:-1]) > 1 :
			print(line)