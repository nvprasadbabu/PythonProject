# OOPS concepts

# Github location: https://github.com/CoreyMSchafer/code_snippets/tree/master/Object-Oriented

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        return '{} {}'.format(self.name, self.age)
        #print(self.name)
        #print(self.age)

p1 = Person("John", 25)
p2 = Person("Bob", 30)

print(p1.display())
print(p2.display())
print(Person.display(p1))
print(Person.display(p2))

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@email.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())



## Inheritance
class Developer(Employee):
    raise_amount = 1.10
    def __init__(self, first, last, pay, prog_lang):
        #Employee.__init__(self, first, last, pay)
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        self.employees.append(emp)

    def remove_emp(self, emp):
        self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('===>', emp.fullname())

## Property Decorators
class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Person('John', 'Smith')
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname



#============================================
print(Employee.num_of_emps)
emp1 = Employee('John', 'Doe', 50000)
emp2 = Employee('Bob', 'Doe', 65050)
print(emp1.fullname())
print(emp2.fullname())
print(Employee.num_of_emps)
# print(Employee.__dict__)
# print(emp1.__dict__)

print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
#emp2.raise_amount = 1.1
Employee.set_raise_amount(1.05)
emp2.apply_raise()
print(emp2.pay)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

#first, last, pay = emp_str_1.split('-')

#new_emp_1 = Employee(first, last, pay)
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_2.email)
print(new_emp_2.pay)

import datetime
my_date = datetime.datetime.now()
print(Employee.is_workday(my_date))
print(my_date.strftime("%m/%d/%Y"))

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2) # __add__ method in the class

print(len(emp_1)) # __len__

