# Thực hành 1
def intersection (nums1: list, nums2: list):
    intersection_arr = []
    for n in nums1:
        if n in nums2 and n not in intersection_arr:
            intersection_arr.append(n)

    return intersection_arr

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
result = intersection(nums1, nums2)
print(result)


# Thực hành 2
def sap_xep_mau(color1, color2):
    # r < w < b
    if color1 == color2:
        return False
    if color1 == "r":
        return True
    if color1 == "w" and color2 == "b":
        return True
    return False

def sap_xep_bong(nums: list):
    n = len(nums)
    for i in range (n):
        for j in range (n - i - 1):
            if sap_xep_mau(nums[j + 1], nums[j]):
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

nums = ["b", "r", "b", "w", "w", "r"]
result1 = sap_xep_bong(nums)
print(result1)