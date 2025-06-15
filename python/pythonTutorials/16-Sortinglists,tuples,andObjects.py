#List Sorting
li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li)

s_Li_desc = sorted(li, reverse=True)
print('Sorted Variable:\t', s_li)

li.sort()
print(s_Li_desc)

print('Original Variable:\t', li)

#Tuple sorting

tup = (9,1,8,2,7,3,6,4,5)
s_tup = sorted(tup)
print('Tuple\t', s_tup)

#Dictionary Sorting
di = {'name': 'Corey', 'job': 'Programming', 'age': None, 'os': 'Mac'}
s_di = sorted(di)
print('Dict\t', s_di)

li = [-6,-5,-4,1,2,3]
s_li = sorted(li, key = abs)
print(s_li)

class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)
    
e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.name

s_employees = sorted(employees, key = e_sort, reverse=True)
s_employees1 = sorted(employees, key=lambda e: e.age)
print(s_employees1)
