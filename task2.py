def comparision(a,b,c,d):
	if a>b:
		if a>c:
			comparision(a,b,c,d)
			if a>d:
				print("THe largest number is:",a)
	elif b>a:
		if b>c:
			comparision(a,b,c,d)
			if b>d:
				print("The largest number is:",b)
	elif c>a:
		if c>b:
			comparision(a,b,c,d)
			if c>d:
				print("The largest number is:",c)
	else:
		print ("The largest number is:",d)

comparision(1,2,3,2)
