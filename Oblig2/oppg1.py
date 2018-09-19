import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

electron_mass = 9.11e-31                    #[kg]
electron_charge = -1.6e-19                  #[C]

electric_field = np.array([-5.0, 0, 0])     #[N/C]

total_time = 1e-6

force = electron_charge*electric_field
acceleration = force/electron_mass

def integrate(dt):
    total_time_steps = int(total_time/dt)

    positions = np.zeros((3, total_time_steps))
    velocities = np.zeros((3, total_time_steps))

    for t in range(total_time_steps-1):
        velocities[:, t+1] = velocities[:, t] + acceleration*dt
        positions[:, t+1] = positions[:, t] + velocities[:, t+1]*dt

    return positions

def plot3d(positions):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlabel("x[m]")
    ax.set_ylabel("y[m]")
    ax.set_zlabel("z[m]")

    ax.plot(positions[0, :], positions[1, :], positions[2, :])

    ax.legend(["dt = 1ns", "dt = 100ns"])

    plt.show()

def plot2d(positions):
    #Numerical
    time = np.linspace(0, total_time-total_time/len(positions[0, :]), len(positions[0, :]))
    plt.plot(time, positions[0, :])

    #Analytical
    plt.plot(time, 0.5*acceleration[0]*time**2)

    plt.xlabel("time[s]")
    plt.ylabel("position[m]")

    plt.legend(["Numerical position", "Analytical position"])
    plt.show()




plot2d(integrate(1e-7))
