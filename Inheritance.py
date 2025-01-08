#1. Write a python program to Create Student Class

class Student:
    def __init__(self, id, name, age, gender):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def __del__(self):
        print("object destroyed")

    def show_details(self):
        print(f"student id :{self.id}")
        print(f"student name :{self.name}")
        print(f"student age :{self.age}")
        print(f"student gender :{self.gender}")


ids = input("Enter Id of Student : ")
nam = input("Enter Name of Student :")
ag = input("Enter age of student : ")
gen = input("Enter gender of student : ")
new_student = Student(ids, nam, ag, gen)
# new_student.setdata()

new_student.show_details()


#Create a Parent Class Create a class named Person, with firstname and lastname properties, and a printname method:

class Person:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print(self.firstname, self.lastname)


newPerson = Person("Sam", "Pradhan")
newPerson.printname()


#Create a Child Class

class Student(Person):
    def __init__(self, fname, lname, year):
        # Person.__init__(self, fname, lname)
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print(self.firstname, self.lastname, self.graduationyear)


newStudent = Student("John", "K", 2013)
newStudent.printname()
newStudent.welcome()

#Add the __init__() Function to Child class
#Use the super() Function
#Add a property called graduationyear to the Student class:

#4. Write a python program to Implement Abstraction using Abstract class
