import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(-5, 5, 100)
y = x**2 / np.sin(x/2)

ax.plot(x,y)

plt.show()
