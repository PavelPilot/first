import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-40,40,10000)
y = x**3 # Сама функция
y1 = x**2 # Вторая функция
plt.figure(1)
plt.xlabel('ось х')
plt.ylabel('ось y')
plt.grid()
plt.axis([-4, 4, -8, 8]) #xmin xmax ymin ymax
plt.plot(x,y, linewidth = 3, color='green',marker='o', markersize = 2) #, linestyle = 'dashed')
plt.plot(x,y1, linewidth = 3, color='red') # Отображение второй ф-ции
plt.show()

