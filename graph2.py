import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4,5] # Точки на оси Х
y = [25,32,34,20,25] # Точки на оси Y
plt.xlabel('ось х')
plt.ylabel('ось y')
plt.plot(x,y, color='green', marker='o', markersize = 7, linewidth = 3) # Выделение точек
plt.grid()
# plt.title('Первый график') # Заголовок графика
plt.plot(x,y)
plt.show()
