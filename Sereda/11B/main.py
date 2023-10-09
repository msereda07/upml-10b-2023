import matplotlib.pyplot as plt
import numpy as np

n=9

x = np.linspace(0,n*2.5, 150)
y = np.linspace(0,n*2.5, 150)

a, b = np.meshgrid(x, y)

C1 = (a - n) ** 2 + (b - n) ** 2 - (n/2) ** 2
C2 = (a - n) ** 2 + (b - n) ** 2 - (n/(2**0.5)) ** 2

line1 =  (a - n)-(b - n)+n/(2**0.5)
line2 = -(a - n)-(b - n)+n/(2**0.5)
line3 =  (a - n)-(b - n)-n/(2**0.5)
line4 = -(a - n)-(b - n)-n/(2**0.5)

figure, axes = plt.subplots()

axes.contour(a, b, C1, [0], colors='b', label='Circle 1')
axes.contour(a, b, C2, [0], colors='r', label='Circle 2')

axes.contour(a, b, line1, [0], colors='g', label='Line 1')
axes.contour(a, b, line2, [0], colors='g', label='Line 2')
axes.contour(a, b, line3, [0], colors='g', label='Line 3')
axes.contour(a, b, line4, [0], colors='g', label='Line 4')

axes.set_aspect(1)

plt.show()