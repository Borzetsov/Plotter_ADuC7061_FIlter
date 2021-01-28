import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

x = np.linspace(-5, 5, 100)
y = x**2 / np.sin(x/2)
z = np.sin(x)

ax.plot(x,y,z)

plt.show()
