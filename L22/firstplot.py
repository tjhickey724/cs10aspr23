from matplotlib import pyplot as plt
import numpy as np
x = np.arange(0, 5, 0.1)
y = np.sin(x)
plt.plot(x, y)
plt.grid()
plt.title("Sine function",fontsize=32)
plt.xlabel("radians")
plt.ylabel("function value")
plt.show()