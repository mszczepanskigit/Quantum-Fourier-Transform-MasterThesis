"""
Exploring Classical and Quantum Fourier Transforms: A Practical Comparative Perspective utilizing IBM Quantum Platform
File: test_2-2.py
Author: Mateusz Szczepański
Date: 05.09.2023
Description: Extra check-in's for classical analysis performed for Problem 2 in Section 4.5.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import fft
mpl.rcParams.update(mpl.rcParamsDefault)

x = [4*k/64 for k in range(64)]
f = np.zeros(64, dtype=complex)

a = 1/np.sqrt(2)
f[4] = a
f[60] = a
#print(np.sum(f**2))

f2 = fft.fft(f)

plt.scatter(x, np.real(f2), c="purple")
plt.xlabel(r"Given nodes $x_k$")
plt.ylabel(r"Reconstructed values")
plt.title(r"FFT performed on $\tilde{\xi}$")
plt.show()