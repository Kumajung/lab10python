# Example 13 ตัวอย่างการสร้างเซตด้วย Set-Builder Notation
# เซตของเลขคู่ที่น้อยกว่าหรือเท่ากับ 20
even_numbers = {x for x in range(21) if x % 2 == 0}
print("Set of even numbers less than or equal to 20:", even_numbers)