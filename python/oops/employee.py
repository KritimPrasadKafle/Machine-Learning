class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

e1 = Employee("Kritim", 20)
e2 = Employee("Kafle", 30)

print("",  e1.name)
print("", e2.name)

class Teacher:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def raise_salary(self, percentage):
        self.salary = self.salary * (100 + percentage) / 100


t1 = Teacher("Hello", "Hi", 234)
t1.raise_salary(12)
print("", t1.salary)
t2 = Teacher("Hi", "Hey", 2387324)
print("", t1.get_full_name())
print("", t2.get_full_name())

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}, ${self.price}"
    def __repr__(self):
        return f"{self.name} ({self.product_id})"
    

products = [
    Product(1, "Headphones", 33),
    Product(2, "Monitor", 34),
    Product(4, "Soundcard", 32)
]

for p in products:
    print("", p)
    print("", str(p))
    print("", repr(p))
    print()

class Employee1:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def get_info(self):
        return f"Employee {self.name}, salary{self.salary}"
    

class Manager(Employee1):
    pass

e = Employee1("Chuck", 1800)
m = Manager("Vera", 2000)

print("", dir(e))
print("", dir(m))
    