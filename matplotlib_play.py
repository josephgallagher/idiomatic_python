from pylab import *
from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 10)
fig, ax = plt.subplots()

ax.plot(x, x**2, label="y = x**2")
ax.plot(x, x**3, label="y = x**3")
ax.legend(loc=9) # upper left corner
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')
plt.show()

# x = np.linspace(-10, 10, 10)
# y = x ** 3
#
# fig = plt.figure()
#
# axis1 = fig.add_axes([0.1, 0.1, 1.0, 1.0])
# axis2 = fig.add_axes([0.8, 0.25, 0.4, 0.3])
#
# axis1.plot(x, y, 'yellow')
# axis1.set_xlabel('x')
# axis1.set_ylabel('y')
# axis1.set_title('big title')
#
# axis2.plot(x, y, 'orange')
# axis2.set_xlabel('x')
# axis2.set_ylabel('y')
# axis2.set_title('tiny title')
#
# plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
# plt.show()

