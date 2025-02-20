# Example 17 ตัวอย่างการตรวจสอบ Subset และ Proper Subset
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
is_subset = A.issubset(B)
is_proper_subset = A.issubset(B) and A != B
print("Is A a subset of B?", is_subset)  # ผลลัพธ์: True
print("Is A a proper subset of B?", is_proper_subset)  # ผลลัพธ์: True