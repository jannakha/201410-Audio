#DFT implementation for a real sinusoid

import numpy as np
import matplotlib.pyplot as plt

N = 64 #size of signal
fq = 7.5	#frequency/period
x = np.cos(2 * np.pi * fq / N * np.arange(N))

X = np.array([])

nv = np.arange(-N/2, N/2)
kv = np.arange(-N/2, N/2)

for k in kv:
	s = np.exp(1j * 2 * np.pi * k / N * nv)
	X = np.append(X, sum(x * np.conjugate(s)))

#restore original signal from DFT (X)
y = np.array([])
for n in nv:
	s = np.exp(1j * 2 * np.pi * n / N * kv)
	y = np.append(y, 1.0 / N * sum(X * s))

plt.plot(kv, abs(X))	#DFT
plt.plot(kv, y)			#Original signal

plt.axis([-N/2, N/2 - 1, -N/2, N/2])
plt.xlabel("Indexes")
plt.ylabel("Amplitube")
plt.show()

