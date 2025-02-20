# ตัวอย่าง 26 Complement ของเซต โจทย์ กำหนด Universal 
#  จงหาค่าของ 𝐴 ′ A ′ (Complement ของ A)
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

# กำหนดเซต
U = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13}
A = {2, 4, 6, 9, 13}

# สร้าง Venn Diagram
v = venn2(subsets=(len(U-A), len(A-U), len(A&U)), set_labels=('Set U', 'Set A'))

# ปรับสีของ Venn Diagram
v.get_patch_by_id('100').set_facecolor('blue')
v.get_patch_by_id('110').set_facecolor('red')
v.get_patch_by_id('010').set_facecolor('green')

# แสดง Venn Diagram
plt.title("Venn Diagram of U and A")
plt.show()