'''1. Đánh giá thuật toán và thời gian của thuật toán'''
# import time

# def is_prime(n: int):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# number = 999999937 # Số nguyên tố lớn nhất có 9 chữ số

# begin = time.time()
# result = is_prime(number)
# end = time.time()

# print(number, "is prime" if result else "is not prime")
# print("Algorithm took", end - begin, "seconds")


import time

def is_prime(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = 999999937

begin = time.time()
result = is_prime(number)
end = time.time()

print(number, "is prime" if result else "is not prime")
print("Algorithm took", end - begin, "seconds")

'''4. Ví dụ 3: Đánh giá độ phức tạp của thuật toán sau'''

n = int(input("Nhập n: "))
arr = [] 
for i in range(1, n + 1): 
    i = int(input()) 
    arr.append(i) 

arr.sort()
found = False 
for i in range(len(arr) - 1): 
    if arr[i] == arr[i + 1]: 
        print("True")
        found = True
        break

if not found:
    print("False")


nums = [1, 2, 3, 1, 2, 2, 5]
def test(nums):
    for i in range (len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
                break
    return False

if test(nums):
    print("Yes")
else:
    print("No")

def test_sort(a):
    a.sort()
    for i in range(len(a) - 1):
        if a[i] == a[i + 1]:
            return True
    return False