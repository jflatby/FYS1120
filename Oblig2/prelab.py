import numpy as np
import matplotlib.pyplot as plt

data = np.array([[1,2,3,4,5,6,7,8,9,10],
                [1,3,5,7,9,7,5,3,1,0]])

def get_polynomial(x, coeffitients):
    poly = 0
    degree = len(coeffitients)-1
    return sum(coeffitients[i]*x**(degree-i) for i in xrange(len(coeffitients)))


def least_squares_fit(data, degree):
    coeff = np.polyfit(data[0], data[1], degree)
    plt.scatter(data[0], data[1])

    x = np.linspace(np.min(data), np.max(data), 100)
    plt.plot(x, get_polynomial(x, coeff))
    plt.show()

least_squares_fit(data, 2)