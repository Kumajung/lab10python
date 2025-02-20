# Example 19 ตัวอย่างการคำนวณ Union, Intersection, และ Difference
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

union = A.union(B)
intersection = A.intersection(B)
difference = A.difference(B)

print("Union of A and B:", union)  # ผลลัพธ์: {1, 2, 3, 4, 5, 6}
print("Intersection of A and B:", intersection)  # ผลลัพธ์: {3, 4}
print("Difference of A and B:", difference)  # ผลลัพธ์: {1, 2}