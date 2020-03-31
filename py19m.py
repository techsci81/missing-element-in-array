# Python program to find out missing elements from master array
import numpy as np 
testarray = np.array([4,3,2,5,7,9,11,12,13])
masterarray = np.array([2,3,4,5,9,10,14])
tsize = testarray.size
msize = masterarray.size
presentnew = []
present = []
absent = []
for i in range (masterarray.size):
	t = masterarray[i]
	for i in range (testarray.size):
		if t == testarray[i]:
			present.append(t)
			presentnew = testarray[(i+1):(testarray.size)]

for i in range (len(present)):
	a = present[i]
	for i in range (masterarray.size):
		if a == masterarray[i]:
			absent = masterarray[(i+1):(masterarray.size)]

print('present in testarray', present)
print('missing in testarray', absent)
print('present in testarray but not in master',presentnew)
