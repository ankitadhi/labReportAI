def SumList():
    list = [1,2,3,4, 5]
    sum = 0
    for i in list:
        sum += i  
    return sum
sum = SumList()
print(sum)