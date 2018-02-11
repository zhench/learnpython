# -*-coding:utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

a = plt.subplot(1,1,1)
x = np.arange(0.,3.,0.1)

#这里b表示blue，g表示green，r表示red，-表示连接线，--表示虚线链接
a1 = a.plot(x, x, 'bx-', label = 'line 1')
a2 = a.plot(x, x**2, 'g^-', label = 'line2')
a3 = a.plot(x, x**3, 'gv-', label = 'line3')
a4 = a.plot(x, 3*x, 'ro-', label = 'line4')
a4 = a.plot(x, 2*x, 'r*-', label = 'line5')
a4 = a.plot(x, 2*x+1, 'ro--', label = 'line6')

#标记图的题目，x和y轴
plt.title("My matplotlib learning")
plt.xlabel("X")
plt.ylabel("Y")


#显示图例
handles, labels = a.get_legend_handles_labels()
a.legend(handles[::-1], labels[::-1])
plt.show()