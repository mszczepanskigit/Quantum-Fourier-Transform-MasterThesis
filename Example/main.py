"""
Exploring Classical and Quantum Fourier Transforms: A Practical Comparative Perspective utilizing IBM Quantum Platform
File: main.py
Author: Mateusz Szczepański
Date: 05.09.2023
Description: Script that allowed to visualize the corrupted signal reconstruction in Example 1.27.
"""

from scipy.stats import expon
from scipy import fft
import numpy as np
import matplotlib.pylab as plt
from scipy.interpolate import make_interp_spline
import matplotlib as mpl
from matplotlib.animation import FuncAnimation

mpl.rcParams.update(mpl.rcParamsDefault)
np.random.seed(0)
x = np.array([x for x in range(64)])
s_original = np.array(x * np.sin(0.39 * x) ** 2)
s = s_original.copy()
s[16:40] = 0
# \frac{1}{5}x\sin^{2}\left(0.39x\right)\left\{0\le x<48\right\}
# print(s[1:5])
s_hat_abs = np.abs(fft.fft(s))
s_hat = fft.fft(s)

"""fig, axs = plt.subplots(1, 2, figsize=(12, 4))

# Plot the first figure on the left subplot
axs[0].plot(x, s, color='blue')
axs[0].set_xlabel('n')
axs[0].set_ylabel(r"$s(n)$")
axs[0].set_title('Corrupted signal')

axs[1].plot(x, s_hat_abs, color='red')
axs[1].set_xlabel('k')
axs[1].set_ylabel(r"$\left|\hat{s}(k)\right|$")
axs[1].set_title('Fourier transform of the corrupted signal')"""
# plt.show()
# plt.savefig('s_and_s-hat.png')

s_hat[9:] = 0
varsigma = np.abs(fft.ifft(s_hat))
"""plt.plot(x, s, color='lightblue', label="corrupted signal")
plt.plot(x, varsigma, color='green', label="recovered signal")
plt.legend(loc="upper left")
plt.title(r"Recovered function s(n) after cutting frequencies for $k\geq 10$")
plt.xlabel("n")
plt.ylabel(r"$\varsigma (n)$")
plt.savefig('recovered_s.png')"""
s_1 = np.zeros(64)
for i in range(64):
    if 16 <= i < 40:
        s_1[i] = varsigma[i]
    else:
        s_1[i] = s[i]

s_1_hat = fft.fft(s_1)
s_1_hat_abs = np.abs(s_1_hat)
s_1_hat[9:] = 0
varsigma_1 = np.abs(fft.ifft(s_1_hat))

final = np.zeros(64)
for i in range(64):
    if 16 <= i < 40:
        final[i] = varsigma_1[i]
    else:
        final[i] = s[i]

plt.plot(s_original, color='green', label="Original signal")
plt.plot(s, color='lightblue', label="Original corrupted signal")
plt.plot(final, color='red', label="Final signal after 2 iterations of the DFT")
plt.title("Final result of a signal compared to the original one and the corrupted one")
plt.legend(loc="upper left")
plt.xlabel("n")
plt.ylabel(r"Final signal values")
plt.show()
