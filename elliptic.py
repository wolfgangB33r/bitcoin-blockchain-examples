#
# Python script for plotting an elliptic curve
#
import numpy as np
import matplotlib.pyplot as plt

a = 0
b = 7
    
y, x = np.ogrid[-5:5:100j, -5:5:100j]
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * a - b, [0])
plt.grid()
plt.show()
