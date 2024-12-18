def getDivision(percentage):
    if percentage >= 80:
        return "Distinction"
    elif percentage >= 65:
        return "First Division"
    elif percentage >= 55:
        return "Second Division"
    elif percentage >= 40:
        return "Third Division"
    else:
        return "Fail"

