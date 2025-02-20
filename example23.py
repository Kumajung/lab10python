# Example 23 ตัวอย่างการคำนวณลำดับเรขาคณิต
# ลำดับ: 2, 6, 18, 54, ...
n = 4  # จำนวนเทอม
first_term = 2
common_ratio = 3
geometric_sequence = [first_term * (common_ratio ** (i-1)) for i in range(1, n+1)]
print("Geometric Sequence:", geometric_sequence)  # ผลลัพธ์: [2, 6, 18, 54]