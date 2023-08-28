import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import fft
mpl.rcParams.update(mpl.rcParamsDefault)

sequence = "AAATGCTCGCCGCATGCTCTGATGTAGTAGTCCCATGCTTTTGCTATGCTATGCTACAGTACTG"

conversion = {"A": 1, "C": 2, "G": 3, "T": 4}

numeric_sequence = [conversion[i] for i in sequence]
alpha = numeric_sequence
numeric_sequence2 = [str(conversion[i]) for i in sequence]
#print(''.join(numeric_sequence2))

"""plt.plot(range(64), alpha, c="olive")
plt.xlabel("Sequence order")
plt.ylabel("Numeric value")
plt.ylim(0.5, 4.5)
plt.yticks([1, 2, 3, 4])  # Set the y-axis ticks to your desired values
plt.title(r"Numeric representation of the sequence $|\alpha\rightangle$")
plt.show()"""

#print(sigma)
Falpha = fft.fft(alpha)
#print(np.abs(Fsigma))

"""plt.plot(range(64), np.abs(Falpha)**2, c="olive")
plt.xlabel("Frequencies")
plt.ylabel("Squared amplitudes")
plt.title(r"Power spectrum of the sequence $|\alpha\rightangle$")
plt.show()"""

beta = alpha - np.mean(alpha)

Fbeta = fft.fft(beta)
plt.plot(range(64), np.abs(Fbeta)**2, c="olive")
plt.xlabel("Frequencies")
plt.ylabel("Squared amplitudes")
plt.title(r"Power spectrum of the sequence $|\beta\rightangle$")
plt.show()
