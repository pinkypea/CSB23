'''Thuật toán tìm kiếm tuần tự'''
def linear_search(arr:list, num):
    for i in range(len(arr)):
        if arr[i] == num:
            return i
        
arr = [10, 2, 3, 5, -1, 100, -54]
number = 100
result = linear_search(arr, number)
print(result)

'''Thuật toán tìm kiếm nhị phân'''
def binary_search(arr:list, num):
    arr.sort()
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if num < arr[mid]:
            end = mid - 1
        elif num > arr[mid]:
            start = mid + 1
        else: # arr[mid] == num
            return mid
    return -1

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13, 15, 16]
target = 10
result = binary_search(list, target)
print(result)

# Viết một hàm nhận vào một tin nhắn (là một chuỗi văn bản). 
# Hàm sẽ tách tin nhắn đó thành các từ đơn và dùng thuật toán tìm kiếm tuần tự để kiểm tra xem có từ nào nằm trong danh sách từ cấm hay không.
# Nếu phát hiện từ cấm, thay vì trả về chỉ số, hãy trả về chuỗi tin nhắn đó nhưng từ cấm đã bị che đi bằng các ký tự *** (Ví dụ: "bạn này ngốc quá" thành "bạn này *** quá").
# Nếu tin nhắn "sạch", giữ nguyên văn bản.

def scan_words(message, banned_words):
    words = message.split()
    for i in range(len(words)):
        for j in range(len(banned_words)):
            if words[i].lower() == banned_words[j].lower():
                words[i] = "***"

    clean_message = " ".join(words)
    return clean_message

banned_words = ["ngu", "dan", "ga"]
message = "may con ga dan don"
result = scan_words(message, banned_words)
print(message)
print(result)

# Bài 2
# danh_sach_nguoi_choi = [1000, 1500, 1300, 1420, 1500, 1540, 1600]
# mmr = 1400
# Sử dụng thuật toán tìm kiếm nhị phân.
# Tìm ra người chơi có số điểm mmr cao hơn và gần mình nhất.

def tim_doi_thu(danh_sach_nguoi_choi, mmr):
    start = 0
    end = len(danh_sach_nguoi_choi) - 1
    best_situation = - 1

    while start <= end:
        middle = (start + end) // 2
        if danh_sach_nguoi_choi[middle] >= mmr:
            best_situation = middle
            end = middle - 1
        else:
            start = middle + 1

    return danh_sach_nguoi_choi[best_situation]

danh_sach_nguoi_choi = [1000, 1200, 1300, 1420, 1500, 1540, 1600]
mmr = 1400

result1 = tim_doi_thu(danh_sach_nguoi_choi, mmr)
print(result1)