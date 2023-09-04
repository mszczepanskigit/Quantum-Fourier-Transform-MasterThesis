"""
Exploring Classical and Quantum Fourier Transforms: A Practical Comparative Perspective utilizing IBM Quantum Platform
File: test_2.py
Author: Mateusz Szczepański
Date: 05.09.2023
Description: Classical analysis performed for Problem 2 in Section 4.5.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import fft
mpl.rcParams.update(mpl.rcParamsDefault)

x = [4*k/64 for k in range(64)]
f = np.sin(2*np.array(x)*np.pi)

f[16:32] = 0

f = f/np.linalg.norm(f)

f_fft = fft.fft(f)

f_fft[np.abs(f_fft) <= 4] = 0

f2 = fft.ifft(f_fft)

#print(np.sum(f**2))
"""plt.scatter(x, f, c="cyan")
plt.xlabel(r"Given nodes $x_k$")
plt.ylabel(r"$\sin(2\pi x_k)$")
plt.title(r"Normalized vector of values after zeroing $k=16,\dots,32$ within $64$ nodes")
plt.show()"""

"""plt.scatter(x, np.abs(f_fft), c="cyan")
plt.xlabel(r"Frequencies")
plt.ylabel(r"$|\mathcal{F}(xi)|$")
plt.title(r"Absolute values of the frequencies")
plt.show()"""

"""plt.scatter(x, f2, c="cyan")
plt.xlabel(r"Given nodes $x_k$")
plt.ylabel(r"Reconstructed values")
plt.title(r"Reconstructed signal after proper frequencies selection")
plt.show()"""
print(np.sum(f2**2))