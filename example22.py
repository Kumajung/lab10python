# Example 22 ตัวอย่างการคำนวณลำดับเลขคณิต
# ลำดับ: 1, 3, 5, 7, 9, ...
n = 5  # จำนวนเทอม
first_term = 1
common_difference = 2
arithmetic_sequence = [first_term + (i-1)*common_difference for i in range(1, n+1)]
print("Arithmetic Sequence:", arithmetic_sequence)  # ผลลัพธ์: [1, 3, 5, 7, 9]