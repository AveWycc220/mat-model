from numpy import sqrt
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('D:\\Projects\\mat model\\1 lab\\OGZPY.csv')
plt.scatter([i for i in range(0, len(data['Close']))], data['Close'])
plt.xlabel('Дни')
plt.ylabel('Цена')
plt.show()
price = data['Close'][0:100]
temp_m = []
m = []
for i in range(0, len(price)):
    for j in range(0, len(temp_m)):
        if price[i] > temp_m[j]:
            if j == len(temp_m) - 1:
                m.append(1)
        else:
            m.append(0)
            break
    temp_m.append(price[i])
temp_l = []
l = []
for i in range(0, len(price)):
    for j in range(0, len(temp_l)):
        if price[i] < temp_l[j]:
            if j == len(temp_l) - 1:
                l.append(1)
        else:
            l.append(0)
            break
    temp_l.append(price[i])
d = [0 for _ in range(0, len(m))]
for i in range(0, len(m)):
    d[i] = (m[i] - l[i])
D = sum(d)
t_nabl = D/2.894
p = {'0.05' : 12.7, '0.01': 63.65, '0.001': 636.61}
print(t_nabl)