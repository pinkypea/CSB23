'''1. Set'''
# Khai báo
fruit_basket = {"apple", "banana", "orange", "cherry"}
print(fruit_basket)

# Truy cập
for fruit in fruit_basket:
    print(fruit)

# Thêm
fruit_basket.add("pinapple")
fruit_basket.update({"peach", "grapes"})

# Xóa
fruit_basket.remove("pinapple")
fruit_basket.discard("peach")

# Phép hợp
lunch = {"soup", "sandwich", "omelet"}
dinner = {"soup", "steak", "pho"}
# meals = lunch.union(dinner) O(m+n)
meals = lunch | dinner
print(meals)

# Phép giao
laptops = {"lenovo", "samsung", "dell"}
phones = {"apple", "samsung", "vivo"}
# elec_devices = laptops.intersection(phones) O(min(m, n))
elec_devices = laptops & phones
print(elec_devices)

# Phép trừ
cars = {"vinfast", "tesla", "toyota"}
motobikes = {"honda", "vinfast", "yamaha"}
# vehicles = cars.difference(motobikes)
vehicles = cars - motobikes
print(vehicles)

'''2. Ánh xạ'''
gpa_10 = [5.0, 7.0, 8.0, 10.0, 9.0]
def convert_gpa (score):
    return score / 10 * 4

gpa_4 = map(convert_gpa, gpa_10)
print(list(gpa_4))

# Dictionary
# Khởi tạo
phone_book = {}
# phone_book = dict()

phone_book['Alice'] = "1234567890"
phone_book["John"] = "0987654321"
phone_book["Bob"] = "5555555555"

# Truy xuất
print(phone_book.get("Bob"))

# Xóa
del phone_book['Bob']

# Thực hành
text = input("Enter text: ")
words_list = text.lower().split()

# Cách 1: Dùng Dictionary
count_words = {}
for word in words_list:
    if word in count_words:
        count_words[word] += 1
    else:
        count_words[word] = 1

print(count_words)

# Cách 2: Set + Dictionary
word_set = set(words_list)
word_count_set = {}
for word in word_set:
    word_count_set[word] = words_list.count(word)

print(word_count_set)