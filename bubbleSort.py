# bubble sort algorithem 

# create variable contains lisf of number unsorted 
number = [44,33, 2, 6,3,1]
def bubbleSort(value):
	for i in range(len(value)):
		for j in range(len(value)):
			if value[j] == value[len(value)-1]:
				break
			if value[j] > value[j+1]:
				temp = value[j]
				value[j] = value[j+1]
				value[j+1] = temp
	return value #return value after doing nested looping 


sort = bubbleSort(number)
print(sort)
