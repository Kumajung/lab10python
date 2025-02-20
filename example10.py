# Example 10 ตัวอย่างการใช้ Set-Builder Notation
# สร้างเซตของเลขคี่ที่น้อยกว่าหรือเท่ากับ 15
odd_numbers = {x for x in range(16) if x % 2 != 0}
print("Set of odd numbers less than or equal to 15:", odd_numbers)