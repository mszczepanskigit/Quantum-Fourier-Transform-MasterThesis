import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import fft
mpl.rcParams.update(mpl.rcParamsDefault)

x = [4*k/16 for k in range(16)]
f = np.sin(2*np.array(x)*np.pi)

f[5:8] = 0

f = f/np.linalg.norm(f)
#print(f)
#print(np.sum(f**2))

#print(np.sum(f**2))
f_fft = fft.fft(f)

f_fft[0:4] = 0
f_fft[5:12] = 0
f_fft[13:] = 0

f2 = fft.ifft(f_fft)
#print(np.sum(np.abs(f2)))
"""plt.scatter(x, np.abs(f_fft), c="blue")
plt.xlabel(r"Frequencies")
plt.ylabel(r"$|\mathcal{F}(\psi)|$")
plt.title(r"Absolute values of the frequencies")
plt.show()"""
print(np.sum(f2**2))
"""plt.scatter(x, f2, c="blue")
plt.xlabel(r"Given nodes $x_k$")
plt.ylabel(r"Reconstructed values")
plt.title(r"Reconstructed signal after proper frequencies selection")
plt.show()"""