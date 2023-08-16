import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import fft
mpl.rcParams.update(mpl.rcParamsDefault)

x = [4*k/64 for k in range(64)]
f = np.sin(2*np.array(x)*np.pi)

f[16:32] = 0

f = f/np.sum(f**2)

f_fft = fft.fft(f)

f_fft[np.abs(f_fft) <= 0.8] = 0

f2 = fft.ifft(f_fft)

print(np.sum(np.abs(f2)))
plt.scatter(x, f2, c="cyan")
plt.xlabel(r"Given nodes $x_k$")
plt.ylabel(r"Reconstructed values")
plt.title(r"Reconstructed signal after proper frequencies selection")
plt.show()

"""plt.scatter(x, f, c="cyan")
plt.xlabel(r"Given nodes $x_k$")
plt.ylabel(r"$\sin(2\pi x_k)$")
plt.title(r"Normalized vector of values after zeroing $k=16,\dots,32$ within $64$ nodes")
plt.show()"""