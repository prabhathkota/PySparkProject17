"""
#Create a class called Person with attributes name and age. Add a method display that prints the person's name and age.
"""

"""
class Base1:
    #@classmethod
    def f1(self):
        print ('Base1 f1')
    def f2(self):
        print  ('Base1 f2')

class Base2:
    def f1(self):
        print ('Base2 f1')
    def f2(self):
        print ('Base2 f1')
    def f3(self):
        print ('Base2 f3')

class MultiDerived(Base1, Base2):
    def f1(self):
        print ('MultiDerived f1')

if __name__ == '__main__':
    md = MultiDerived()
    md.f1()  #MultiDerived f1
    md.f2()  #Base1 f2
    md.f3()  #Base2 f3
    #Base1.f1()  #Base1 f1  #classmethod
    #Base2.f1()  #fail
    #MultiDerived.f1()  #fail
"""

class Employee1:
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = sal
    def display(self):
        print("{} - {} - {}".format(self.name, self.age, self.sal))

class Employee2:
    def __init__(self, name, age, sal):
        self.name = name
        self.age = age
        self.sal = sal

    def display(self):
        print("{} - {} - {}".format(self.name, self.age, self.sal))

# class Employee1(Person):
#     def __init__(self, name, age, sal):
#         super().__init__(name, age)
#         self.sal = sal
#
#     def display(self):
#         print("E1 - {} - {} - {}".format(self.name, self.age, self.sal))
#
# class Employee2(Person):
#     def __init__(self, name, age, sal):
#         super().__init__(name, age)
#         self.sal = sal
#
#     def display(self):
#         print("E2 - {} - {} - {}".format(self.name, self.age, self.sal))

class Employee3(Employee1, Employee2):
    def __init__(self, name, age, sal):
        Employee1.__init__(name, age, sal)
        Employee2.__init__(name, age, sal)

    def display3(self):
        print("E3 - {} - {} - {}".format(self.name, self.age, self.sal))

if __name__ == '__main__':
    #p1 = Person('Lak', 34)
    #p1.display()
    e3 = Employee3('Lak1', 34, 50000)
    e3.display()




