# Example 25 ตัวอย่างการคำนวณ Combination และ Permutation
from math import comb, perm

n = 5
k = 2
combination = comb(n, k)
permutation = perm(n, k)

print(f"C({n}, {k}) =", combination)  # ผลลัพธ์: 10
print(f"P({n}, {k}) =", permutation)  # ผลลัพธ์: 20