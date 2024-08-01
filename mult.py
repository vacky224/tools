def mult(num):
	if num == 1:
		return 1
	return num * mult(num - 1)

print (mult(10))
