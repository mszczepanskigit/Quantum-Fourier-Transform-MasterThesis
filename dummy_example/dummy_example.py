import numpy as np
from scipy import fft

x = [i / np.sqrt(30) for i in [1, 2, 3, 4]]

print(x)
print([x2*x2 for x2 in x])

xx = fft.fft(x)

print(xx/np.sum(xx**2))


