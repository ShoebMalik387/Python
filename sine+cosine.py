import matplotlib.pyplot as plt
import numpy as np

x = np.linspace (0,2 * np.pi,100)

sine = np.sin (x)

plt.plot (x, sine, linestyle='--', linewidth=2, color='blue')

plt.title ("sine wave graph", fontsize=14)

plt.xlabel ("Angle is radions", fontsize=12)

plt.ylabel ("value", fontsize=12)

plt.grid ()

plt.show ()