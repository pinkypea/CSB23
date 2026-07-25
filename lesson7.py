'''Thuật toán sắp xếp chọn'''
def selection_sort(arr: list):
    arr_sorted = [] # O(1)
    while arr: # O(n)
        minimum = min(arr) # O(n^2)
        arr_sorted.append(minimum) # O(n^2)
        arr.remove(minimum) # O(n)
    return arr_sorted

my_list = [10, 5, 3, 18, 0, 11]
print(selection_sort(my_list))


'''Thuật toán sắp xếp nổi bọt'''
def bubbles_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_list = [10, 5, 3, 18, 0, 11]
print(bubbles_sort(my_list))

# Bài 1
def selection_sort(arr: list):
    arr_sorted = [] # O(1)
    while arr: # O(n)
        minimum = max(arr) # O(n^2)
        arr_sorted.append(minimum) # O(n^2)
        arr.remove(minimum) # O(n)
    return arr_sorted

diem_spam = [15, 89, 45, 92, 12, 70]
arr_sorted = selection_sort(diem_spam)
print(arr_sorted)

for i in range (len(arr_sorted)):
    if arr_sorted[i] >= 70:
        print(arr_sorted[i])


# Bài 2:
def bubbles_sort(shops: list, prices: list):
    for i in range(len(prices)):
        for j in range(len(prices) - i - 1):
            if prices[j] > prices[j + 1]:
                prices[j], prices[j + 1] = prices[j + 1], prices[j]
                shops[j], shops[j + 1] = shops[j + 1], shops[j]
    return shops, prices

ten_shop = ["Shop A", "Shop B", "Shop C", "Shop D"]
gia_tien = [80, 45, 120, 30]
result = bubbles_sort(ten_shop, gia_tien)
print(result)