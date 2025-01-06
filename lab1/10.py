def largest(list):
    large = list[0]
    for i in list:
        if i>large:
            large = i
        # else:
        #     continue
    return large

list = [12, 5, 18, 2, 9]
largestM =largest(list)
print(largestM) 
