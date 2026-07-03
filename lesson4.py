class Animal:
    tail = "long"
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__sound = "Woof"

    def get_description(self):
        return f"{self.name} is {self.age}-year-old"
    
    def speak(self):
        return self.__sound
    
class Corgi(Animal):
    tail = "short"
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_description(self):
        return f"{self.name} is {self.age}-year-old corgi"
    

# Khởi tạo 1 class Rectangle có 
# - 2 thuộc tính CD và CR.
# - Phương thức get_S để tính diện tích
# - Phương thức get_P để tính chu vi

# Khởi tạo 1 class Triagle là nửa HCN kế thừa từ Rectangle có
# - 2 thuộc tính CD và CR
# - Phương thức get_S để tính diện tích
# - Phương thức get_P để tính chu vi

class Rectangle:
    def __init__(self, cd, cr):
        self.cd = cd
        self.cr = cr

    def get_S(self):
        return self.cd * self.cr
    
    def get_P(self):
        return (self.cd + self.cr) * 2
    
class Triagle(Rectangle):
    def __init__(self, cd, cr):
        super().__init__(cd, cr)

    def get_S(self):
        return self.cd * self.cr * 0.5
    
    def get_P(self):
        ch = (self.cd ** 2 + self.cr ** 2) ** 0.5
        return self.cd + self.cr + ch
    
class TaiKhoanNguoiDung:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def get_infor(self):
        print(self.username)
        print(self.email)

    def change_password(self, new_password):
        self.__password = new_password

class TaiKhoanCreator(TaiKhoanNguoiDung):
    def __init__(self, username, password, email, followers):
        super().__init__(username, email, password)
        self.followers = followers

        # self.followers = 10
    def add_followers(self):
        self.followers += 1

from abc import ABC, abstractmethod
class MonAn(ABC):
    @abstractmethod
    def chuan_bi(self):
        pass

class MonChinh(MonAn):
    def chuan_bi(self):
        print ("Đang chuẩn bị món chính")

class MonPhu(MonAn):
    def chuan_bi(self):
        return ("Đang chuẩn bị món phụ")

'''
Hãy xây dựng một hệ thống trừu tượng PaymentMethod mô phỏng các hình thức thanh toán khác nhau:
1. Thanh toán bằng tiền mặt
2. Thanh toán chuyển khoản
3. Thanh toán quẹt thẻ
'''

from abc import ABC, abstractmethod

# Bước 1: Tạo lớp trừu tượng PaymentMethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass

class CashPayment(PaymentMethod):
    def pay(self, amount) -> None:
        print(f"Thanh toán {amount} bằng tiền mặt")

class BankingPayment(PaymentMethod):
    def pay(self, amount) -> None:
        print(f"Thanh toán {amount} bằng chuyển khoản")

class CardPayment(PaymentMethod):
    def pay(self, amount) -> None:
        print(f"Thanh toán {amount} bằng thẻ")

payment = BankingPayment()
payment.pay(10000)