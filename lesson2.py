# List
fruits = ['apple', "banana", "orange"]
numbers = [1, 2, 3, 4]

print(numbers[2])
print(fruits[0])

# Độ dài của list
print(len(fruits))
print(len(numbers))

# Thay đổi giá trị phần tử
fruits[1] = "pinapple"
print(fruits)

# Xóa phần tử
del numbers[3]
print(numbers)

# Thêm phần tử
numbers.append(10)
print(numbers)

numbers.append([100, 200, 300])
print(numbers)

# Duyệt list
for i in range(len(fruits)):
    print(fruits[i])

# Thực hành: Cho list scores như sau là điểm của các học sinh trong 1 lớp.
# Tính điểm trung bình của lớp đó.
scores = [10, 9, 8, 8.5, 9.5, 7, 6, 9.75]
total = 0
for i in range(len(scores)):
    total += scores[i]

mean = total / len(scores)
print(mean)

# Hàm
def get_frequency(ls: list, value: int):
    count = 0
    for i in ls:
        if i == value:
            count += 1
    return count

print(get_frequency(scores, 8))

def greeting(username: str):
    print("Hello", username)

greeting("Kien")

# Thực hành: 2 bạn A và B chơi 3 cây với nhau.
# Viết hàm để tính số điểm và in ra người chiến thắng.
def ba_cay(list1: list, list2: list):
    total1 = 0
    total2 = 0
    for i in range (len(list1)):
        total1 += list1[i]

    for j in range (len(list2)):
        total2 += list2[j]

    score1 = total1 % 10
    score2 = total2 % 10
    if score1 > score2:
        print("Người thứ nhất chiến thắng")
    elif score1 < score2:
        print("Người thứ hai chiến thắng")
    else:
        print("Hòa")

A = [1, 9, 8]
B = [2, 5, 6]
ba_cay(A, B)

'''ĐỌC VÀ GHI FILE'''
# 1. Mở file
file = open("grades.txt", "r")
file1 = open("grades.txt", "r", encoding="utf-8")

# 2. Đọc file
# Đọc toàn bộ nội dung
content = file.read()

# Đọc 1 dòng
line = file.readline()

# Đọc tất cả các dòng (mỗi dòng là 1 list)
lines = file.readlines()

# 3. Đóng file
file.close()

# 4. Ghi file
file = open("grades.txt", "w")
file.write("9.5")

# 5. Đóng và mở file rút gọn
with open("grades.txt", "w") as file:
    file.write("10")

with open("grades.txt", "r") as file:
    print(file.read())

# 6. Xử lý lỗi
try:
    file = open("grades.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    file.close()


# Sử dụng try-except để đọc file grades.txt.
# Sau đó tính điểm trung bình của các học sinh và in ra file mới là summary