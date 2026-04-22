import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#настройка стиля seaborn
sns.set_theme(style="darkgrid")

#первая ветка функции (0 <= x <= 1)
x1 = np.linspace(0, 1, 200)
y1 = np.cos(x1) * np.exp(-x1**2)

#вторая ветка функции (1 < x <= 2)
x2 = np.linspace(1.01, 2, 200)
y2 = np.log(x2 + 1) - np.sqrt(4 - x2**2)

#точка касания
x0 = 0.5
y0 = np.cos(x0) * np.exp(-x0**2)
k = -np.exp(-x0**2) * (np.sin(x0) + 2 * x0 * np.cos(x0))

#касательная
x_kas = np.linspace(0.2, 1.2, 100)
y_kas = y0 + k * (x_kas - x0)

#построение графика
plt.figure(figsize=(10, 6))

#используем seaborn для построения
sns.lineplot(x=x1, y=y1, linewidth=2.5, label='cos(x)·e^(-x²)', color='blue')
sns.lineplot(x=x2, y=y2, linewidth=2.5, label='ln(x+1) - √(4-x²)', color='green')
sns.lineplot(x=x_kas, y=y_kas, linewidth=2, label='Касательная', linestyle='--', color='red')
sns.scatterplot(x=[x0], y=[y0], s=100, color='red', label='Точка касания')

#настройки
plt.title('График функции и касательная (Seaborn)', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True)
plt.legend()
plt.xlim(0, 2)
plt.ylim(-1.5, 1.5)

#аннотация
plt.annotate(f'({x0}, {y0:.3f})',
             xy=(x0, y0),
             xytext=(x0+0.1, y0+0.1),
             arrowprops=dict(arrowstyle='->'))

plt.show()

print(f'Уравнение касательной: y = {k:.3f}x + {(y0 - k*x0):.3f}')