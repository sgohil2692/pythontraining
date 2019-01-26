def n ():
	res=[i for i in range(1,50) if i%2==0 if i%6==0]
	print len(res)
	print sum(res[5:])
	
g=n()
print g