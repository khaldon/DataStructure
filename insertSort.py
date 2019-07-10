# inseration sort algorithm 
number =  [8,5,2,6,9,3,1,4,0,7]

def insertSort(value):
    for i in range(1, len(value)):
        j = i-1
        while value[j]> value[j+1] and j >= 0:
            value[j], value[j+1] = value[j+1], value[j]
            j -=1

insertSort(number)
print(number)
