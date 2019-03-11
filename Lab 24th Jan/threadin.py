from threading import Thread
from time import sleep

a = 5

def counter( *args):
	global a
	for i in range(5):		
		sleep(1)
		a += 1
		print("Function ", args[0], " says ", a)

threads = []
threads.append(Thread(target=counter, args =[ 1]))
threads.append(Thread(target=counter, args = [ 2]))
threads.append(Thread(target=counter, args = [3]))

for t in threads:
	t.setDaemon(True)
	t.start()

for t in threads:
	t.join(timeout=1)
		
	
	