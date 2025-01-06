from datetime import date


class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = dob  

    def get_age(self):
        birth_date = date.fromisoformat(self.dob)
        print(birth_date)
        today = date.today()
        age =  today.year - birth_date.year 
        #to check whether birthday has come or not this year
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1
        return age

bdate =input("Enter your DOB:")

person = Person("John Doe", "USA", bdate)
age = Person.get_age(person)
print(age)