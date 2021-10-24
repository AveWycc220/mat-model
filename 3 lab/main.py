import numpy as np
import pandas
import matplotlib.pyplot as plt

data = pandas.read_csv('E:\\Projects\\mat-model\\3 lab\\OGZPY.csv')
data_list = list(data['Close'])

x = [i for i in range(len(data_list))]
z = np.polyfit(x, data_list, 3)
f = np.poly1d(z)
plt.legend(['Изначальное', 'Сглаженное'])
plt.plot(x, data_list)
plt.plot(x, f(x))
plt.show()