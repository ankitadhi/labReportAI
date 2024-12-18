def mark():
    marks = []
    for i in range(10):
        
        mark = [int(input(f"Enter marks for student {i+1}: "))]
        marks.append(mark)
    print(marks)
mark()