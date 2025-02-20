# Example 18 ตัวอย่างการสร้าง Venn Diagram ด้วย matplotlib_venn
from matplotlib_venn import venn2
import matplotlib.pyplot as plt

# กำหนดเซต A และ B
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# สร้าง Venn Diagram
venn2([A, B], set_labels=('Set A', 'Set B'))
plt.show()  # แสดง Venn Diagram