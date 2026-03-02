import numpy as np
import matplotlib.pyplot as plt

# Первая ветка функции [0, 1]
x1 = np.linspace(0, 1, 200)
y1 = np.cos(x1) * np.exp(-x1**2)

# Вторая ветка функции (1, 2]
x2 = np.linspace(1.01, 2, 200)
y2 = np.log(x2 + 1) - np.sqrt(4 - x2**2)

# Точка касания
x0 = 0.5
y0 = np.cos(x0) * np.exp(-x0**2)
k = -np.exp(-x0**2) * (np.sin(x0) + 2 * x0 * np.cos(x0))

# Касательная
x_kas = np.linspace(0.2, 1.2, 100)
y_kas = y0 + k * (x_kas - x0)

# Построение графиков
plt.figure(figsize=(10, 6))

# График первой ветки
plt.plot(x1, y1, 'g-', linewidth=2, label='f(x) = cos(x) * e^(-x^2), 0 ≤ x ≤ 1')

# График второй ветки
plt.plot(x2, y2, 'b-', linewidth=2, label='f(x) = ln(x+1) - √(4-x^2), 1 < x ≤ 2')

# Касательная
plt.plot(x_kas, y_kas, '--', color='purple', linewidth=2,
         label=f'Касательная: y = {k:.3f}x + {y0 - k*x0:.3f}')

# Точка касания
plt.scatter(x0, y0, color='red', s=100, zorder=5, label='Точка касания')

# Подпись точки
plt.annotate(f'({x0}, {y0:.3f})',
             xy=(x0, y0),
             xytext=(x0+0.1, y0-0.2),
             fontsize=12,
             bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# Настройки графика
plt.title('График кусочной функции и касательная', fontsize=14, fontweight='bold')
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10, loc='best')
plt.xlim(0, 2)
plt.ylim(-1.5, 1.5)
plt.axhline(y=0, color='black', linewidth=0.5, alpha=0.5)
plt.axvline(x=0, color='black', linewidth=0.5, alpha=0.5)

# Вывод уравнения в консоль
print('=' * 50)
print('РЕЗУЛЬТАТ:')
print('=' * 50)
print(f'Точка касания: ({x0}, {y0:.3f})')
print(f'Производная в точке: {k:.3f}')
print(f'Уравнение касательной: y = {k:.3f}x + {y0 - k*x0:.3f}')
print('=' * 50)

plt.tight_layout()
plt.show()
