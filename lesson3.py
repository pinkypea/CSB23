'''class: Khuôn để tạo ra các objects'''

# Khai báo class
class Dog:
    # Phương thức __init__ để khởi tạo các thuộc tính cho class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Phương thức để in ra thông tin các chú chó
    def display_infor(self):
        print(self.name)
        print(self.age)

# Sử dụng class để khởi tạo object
my_dog = Dog("Rex", 2)
your_dog = Dog("Lu", 3)

print(my_dog.name)
print(my_dog.age)

your_dog.display_infor()

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def display_infor(self):
        print(self.color, self.mileage)

car1 = Car("Xanh", 20000)
car2 = Car("Đỏ", 30000)

car1.display_infor()
car2.display_infor()

# Tạo class có 2 thuộc tính là CD và CR của HCN
# Viết phương thức tính tính Chu vi và Diện tích của HCN

'''Tính đóng gói'''
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sound = "meo meo"

    def speak(self):
        return self.sound
    
my_cat = Cat("Doraemon", 2)
print(my_cat.speak())

'''Tính kế thừa'''
class Laptop:
    def __init__(self, name, ram, cpu):
        self.name = name
        self.ram = ram
        self.cpu = cpu

    def get_information(self):
        print(self.name, self.ram, self.cpu)

class MyLaptop(Laptop):
    def __init__(self, name, ram, cpu, pin, style):
        super().__init__(name, ram, cpu)
        self.name = name
        self.ram = ram
        self.cpu = cpu
        self.pin = pin
        self.style = style

my_laptop = MyLaptop("Lenovo", 16, "Core i5 12th", 1000, "Office")
my_laptop.get_information()


class Item:
    def __init__(self, quantity, price):
        self.quantity = quantity
        self.price = price

class Order(Item):
    def __init__(self, customer_id):
        self.customer_id = customer_id
        self.item_list:list[Item] = []

    def total(self):
        sum = 0
        for i in range (len(self.item_list)):
            sum += self.item_list[i].quantity * self.item_list[i].price
        return sum
    
class Promo(Order):
    def __init__(self, price):
        self.price = price

    def discount(self):
        discount = self.total() * 0.95
        return discount
        
item1 = Item(1, 5)
item2 = Item(1, 10)
item3 = Item(2, 20)

order = Order("0123")
print(order.total())