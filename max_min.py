__author__ = 'waley03'
def maxmin(number):
	mylist = []
	if number != [] and (max(number) != min(number)):
		maximum = max(number)
		minimum = min(number)
		mylist.append(minimum)
		mylist.append(maximum)
		return (mylist)
	elif(max(number) == min(number)):
		length = [len(number)]
		return length
