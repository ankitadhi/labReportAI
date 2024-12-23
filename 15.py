from datetime import date


class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  # dob in "YYYY-MM-DD" format

    def get_age(self):
        birth_date = date.fromisoformat(self.dob)
        today = date.today()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

bdate =input("ENter your DoB")

person = Person("John Doe", "USA", bdate)
age = Person.get_age(person)
print(age)