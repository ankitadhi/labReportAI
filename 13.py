# def find_50th_element():
#     sponsor_sequence = []
#     candidate = 1

#     while len(sponsor_sequence) < 50:
#         # Check divisibility condition
#         if all(candidate % x != 0 for x in sponsor_sequence):
#             sponsor_sequence.append(candidate)
#         candidate += 1

#     return sponsor_sequence[49]  # Return the 50th element (0-indexed)

# result = find_50th_element()
# print(f"The 50th element of the Sponsor sequence is: {result}")

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
