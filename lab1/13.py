def changeCase(string):
    str =' '
    for char in string:
        if char.isalpha():
            if char.isupper():
                str += char.lower()
            elif char.islower():
                str += char.upper()
    return str
str1 = 'hello world'
print(changeCase(str1))
