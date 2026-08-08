# Nhập từ bàn phím 1 danh sách có độ dài n
# n = int(input("Enter array length: "))
# arr = []
# for i in range (n):
#     i = int(input("Enter array value: "))
#     arr.append(i)

# print(arr)

# Chữa bài kiểm tra
# Bài 1
# n = int(input("Enter array length: "))
# arr = []
# for i in range (n):
#     i = int(input("Enter array value: "))
#     arr.append(i)

# found_number = False
# for i in range(n):
#     for j in range (i + 1, n):
#         if arr[i] == arr[j]:
#             print("Số lặp lại là:", arr[i])
#             found_number = True
#             break

# if found_number == False:
#     print("Không có số nào lặp lại")


# Bài 2:
n = int(input("Enter array length: "))
arr = []
for i in range (n):
    i = int(input("Enter array value: "))
    arr.append(i)

for i in range(n):
    for j in range (n - i - 1):
        if arr[j] < arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

print("Điểm cao nhất:", arr[0])

if n < 2:
    print("Không có")
elif n >= 2:
    for i in range (n):
        if arr[i] != arr[0]:
            print("Điểm cao thứ hai:", arr[i])
            break