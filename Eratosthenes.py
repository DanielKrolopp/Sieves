#!/usr/bin/python
#Uses Sieve of Erasthrones

import math
import sys

def eratosthenes():
	print "Starting!"
	i = 2
	file = open("Eratosthenes_output.txt", "w")
	while i < n:
		if i < math.sqrt(n):
			if array[i]:
				k = i
				while k+i < n:
					array[k+i] = False
					k+=i
		if array[i]:
			print(i)
			file.write(`i` + "\n")	
		i+=1
	file.close()
n = 0
try:
	n = mode=int(raw_input("Find primes up to: "))
	print "Allocatng memory..."
	array = [True for a in range(0, n)]
except ValueError:
	print "Enter a valid number."

eratosthenes()
print "Finished generating all primes less than "+`n`+"!"
