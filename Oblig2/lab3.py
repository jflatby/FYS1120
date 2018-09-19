import matplotlib.pyplot as plt
import numpy as np

data_h = np.linspace(0, 0.1, 11)
data_B = [-286, -142, -41.7, -22.2, -12.2, -7.1, -4.3, -2.6, -1.5, -0.8, -0.3]

def Bx(h):
    mu_0 = 4*np.pi * 10**(-7)
    Js = -9e8       #stromtetthet

    print mu_0*Js

    a = 0.017      #radius[m]
    t = 0.01        #tykkelse[m]

    return mu_0/2 * Js * ((h+t)/np.sqrt((h+t)**2 + a**2) - h/np.sqrt(h**2 + a**2))


plt.scatter(data_h, data_B)
plt.plot(data_h, data_B)

h = np.linspace(0, 0.1, 100)
plt.plot(h, Bx(h))

plt.show()

