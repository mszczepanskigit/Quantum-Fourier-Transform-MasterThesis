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