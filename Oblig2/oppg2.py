from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
from mpl_toolkits.mplot3d import Axes3D

style.use("ggplot")

electron_mass = 9.11e-31                    #[kg]
electron_charge = -1.6e-19                  #[C]

magnetic_field = np.array([0, 0, 2])

total_time = 30e-12
dt = 1e-15
total_time_steps = int(total_time/dt)

positions = np.zeros((3, total_time_steps))
velocities = np.zeros((3, total_time_steps))

velocities[:, 0] = np.array([5000, 0, 2000])

def integrate():
    for t in range(total_time_steps-1):
        force = electron_charge * np.cross(velocities[:, t], magnetic_field)
        acceleration = force / electron_mass
        velocities[:, t+1] = velocities[:, t] + acceleration*dt
        positions[:, t+1] = positions[:, t] + velocities[:, t+1]*dt

        if np.absolute(positions[0, t]) < 6e-12 and np.absolute(positions[1, t]) < 4e-11:
            print t
            print positions[:, t]
            print t*dt


    return positions

def plot3d(positions):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    ax.set_xlabel("x [m]")
    ax.set_ylabel("y [m]")
    ax.set_zlabel("z [m]")

    ax.plot(positions[0, :], positions[1, :], positions[2, :])

    ax.legend(["position"])
    plt.savefig("position_plot_2_3d.png")
    plt.show()

def plot2d(positions):
    time = np.linspace(0, total_time-total_time/len(positions[0, :]), len(positions[0, :]))

    plt.plot(time, positions[0, :], time, positions[1, :], time, positions[2, :])

    plt.xlabel("time[s]")
    plt.ylabel("position[m]")

    plt.legend(["x(t)", "y(t)", "z(t)"])

    plt.tight_layout()
    plt.savefig("position_plot_2d.png")
    plt.show()


#plot2d(integrate())
plot3d(integrate())