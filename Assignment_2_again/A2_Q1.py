#0 1 1 2 3 5 8
def f(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return f(n-1)+f(n-2)
	
n=int(raw_input("Enter the number to be get generated in in Fibonacco Series"))
print (map(lambda x:x**3,[f(x) for x in range(n)]))

