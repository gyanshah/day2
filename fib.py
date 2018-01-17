def fib_n(n):
	if n<=1:
		return n
	else:
		return(fib_n(n-1)+fib_n(n-2))

x=int(input("Enter the length of series:"))
for i in range(x):
	 print(fib_n(i)) 
