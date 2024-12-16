class employee:
    def __init__ (self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of the Employe is {self.name} and id is {self.id}")

e1 = employee("Aman",365)
e1.showDetails()

class programmer  (employee):
    def ShowLanguage(self):
        print("Default programming language is python ")

e2 = programmer("Sohail" ,300)
e2.showDetails()
e2.ShowLanguage()


# Inheritance in python
# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.

# Python Inheritance Syntax
# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class
# Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

# Types of inheritance:
#1Single inheritance
#2Multiple inheritance
#3Multilevel inheritance
#4Hierarchical Inheritance
#5Hybrid Inheritance