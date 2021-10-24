from numpy import sqrt
import numpy as np
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('D:\\Projects\\mat model\\2 lab\\OGZPY.csv')
n = 5
n_2 = 11
n_3 = 21  
d = list(data['Close'])
val = 0
new_d = [0 for _ in range(0, len(d))]
for i in range(n, len(d) - n):
    for j in range(i - n, i + n + 1):
        val = val + d[j]
    new_d[i] = val/(2 * n + 1)
    val = 0
ax1 = plt.subplot(311)
ax1.scatter([i for i in range(0, len(data['Close']))], d, linewidths=0.1)
ax1.scatter([i for i in range(0, len(data['Close']))][n:len(d)-n], new_d[n:len(d)-n], linewidths=0.1)
ax1.legend(['Изначальное', 'Сглаженное'])
ax1.set_xlabel('Дни')
ax1.set_ylabel('Цена')
ax1.set_title('n = 5')
val = 0
new_d = [0 for _ in range(0, len(d))]
for i in range(n, len(d) - n_2):
    for j in range(i - n_2, i + n_2 + 1):
        val = val + d[j]
    new_d[i] = val/(2 * n_2 + 1)
    val = 0
ax2 = plt.subplot(312)
ax2.scatter([i for i in range(0, len(data['Close']))], d, linewidths=0.1)
ax2.scatter([i for i in range(0, len(data['Close']))][n_2:len(d)-n_2], new_d[n_2:len(d)-n_2], linewidths=0.1)
ax2.legend(['Изначальное', 'Сглаженное'])
ax2.set_xlabel('Дни')
ax2.set_ylabel('Цена')
ax2.set_title('n = 11')
val = 0
new_d = [0 for _ in range(0, len(d))]
for i in range(n, len(d) - n_3):
    for j in range(i - n_3, i + n_3 + 1):
        val = val + d[j]
    new_d[i] = val/(2 * n_3 + 1)
    val = 0
ax3 = plt.subplot(313)
ax3.scatter([i for i in range(0, len(data['Close']))], d, linewidths=0.1)
ax3.scatter([i for i in range(0, len(data['Close']))][n_3:len(d)-n_3], new_d[n_3:len(d)-n_3], linewidths=0.1)
ax3.legend(['Изначальное', 'Сглаженное'])
ax3.set_xlabel('Дни')
ax3.set_ylabel('Цена')
ax3.set_title('n = 21')
plt.show()

