import matplotlib.pyplot as plt
import numpy as np

import matplotlib.image as mpimg
def sinosoid_sum(x):
    return 2*np.sin(x)-3*np.sin(2*x)+np.sin(3*x)-np.sin(4*x)/2+np.sin(5*x)

x = np.linspace(-10,10,1000)
y=sinosoid_sum(x)
plt.plot(x,y,c="r")
plt.grid(True,which="both")
plt.ylabel("Amplitude")
plt.xlabel("Time")
plt.show()