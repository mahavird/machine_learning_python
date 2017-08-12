x = [1,3,6,10,11,13]
d = [1,0,5,2,1,4]

error_1=0
error_2=0
error_3=0


for i in range(len(d)):
	#print i
	error_1 = error_1 + (2-d[i])**2
	#print error_1


for i in range(len(d)):
	#print i
	error_2 = error_2 + ((x[i]/3.0)-d[i])**2
	#print error_2

for i in range(len(d)):
	#print i
	error_3 = error_3 + ((x[i]%9)-d[i])**2
	#print error_3


print error_1
print error_2
print error_3
