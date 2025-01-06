def sumDict(dict):
    sum = 0
    for key in dict:
        sum += dict[key]
    return sum
dict= {
    'a':100,
    'b':200,
    'c':300,
}
sum = sumDict(dict)
print(sum)
