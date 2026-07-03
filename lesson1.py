# # 1. print()
# print("hello world")
# print(1 + 1)
# print("i am", 15, "years old")

# # 2. input()
# name = input("Enter your name: ")
# print(name)

# tables = int(input("Enter your tables's quantity: "))
# height = float(input("Enter you height: "))

# # 3. Variable
# book_name = "Programming for Dummies"
# year = 2024
# author = ""

# # 4. Data type
# score = 10 # int
# PI = 3.14 # float
# school = "MindX" # string
# passed = True # boolean

# # Thực hành
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# print(a + b, a - b, a * b, a / b)

# 5. Cấu trúc rẽ nhánh if - elif - else
# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# if x > y:
#     print(x)
# elif y > x:
#     print(y)
# else:
#     print("Equal")

# Bạn A và bạn B chơi 3 cây với nhau.
# Mỗi bạn bốc 3 lá bài (trong khoảng 1 - 9).
# Viết chương trình nhập vào 6 số trong khoảng 1 - 9.
# 3 số đầu là bài của bạn A. 3 số sau là bài của bạn B.
# So sánh và in ra kết quả ai thắng.

# Các bước thực hiện
# B1: Nhập 6 số a, b, c, d, e, f
# B2: Tính tổng a + b + c và d + e + f
# B3: Chia lấy dư cho 10
# B4: So sánh và in ra kết quả

# 6. Vòng lặp for
# In ra các số chẵn 1 đến 50
# for i in range(2, 51, 2):
#     print(i)

# 7. Vòng lặp while
# In ra các số từ 1 đến 50
# i = 1
# while i <= 50:
#     print(i)
#     i += 1

# Thực hành
# sum = 0
# n = int(input("Enter number: "))
# while n != -1:
#     sum += n
#     n = int(input("Enter number: "))

# print(sum)

# Nhập vào chương trình số nguyên dương n.
# Tính tổng các ước của n
# B1: Nhập số nguyên dương n
# B2: Khai báo biến sum = 0
# B3: Dùng vòng lặp for từ 1 đến n
# B4: Tìm các ước bằng phép toán %
# B5: Cộng các ước vào biến sum
# B6: In ra biến sum
n = int(input("Enter n: "))
sum = 0
for i in range(1, n + 1):
    if n % i == 0:
        sum += i
# 
print(sum)