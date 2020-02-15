#A function that produces 'num' number of fibonacci numbers
def fibonacci(num):
	x = [1]
	for i in range(1,num):
		if i==1:
			x.append(1)
		else:
			x.append(x[i-2] + x[i-1])
	print(x)
	
