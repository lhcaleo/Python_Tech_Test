def check(x1,x2,x3,x4):
	if(type(x1) is not int or type(x2) is not int or type(x3) is not int or type(x4) is not int):
		raise TypeError("Type Error: input value is not an integer")

	if(x1 == x2 or x3 == x4):
		print("Invalid input: one or more point is given instead of line")
		return False

	# Ensure first point < second point
	x1, x2 = sorted([x1,x2])
	x3, x4 = sorted([x3,x4])

	if(x1 < x3):
		if(x2 <= x3):
			return False
		else:
			return True
	elif(x1 > x3):
		if(x4 <= x1):
			return False
		else:
			return True
	else:
		return True



