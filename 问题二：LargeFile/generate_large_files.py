import random
import numpy as np

f = open('1.txt', 'w')
for i in range(10000000000):
	num = random.randint(1, 10000000000)
	f.write(str(num))
