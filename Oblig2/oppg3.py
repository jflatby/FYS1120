from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as style
from matplotlib.patches import Wedge
from mpl_toolkits.mplot3d import Axes3D

style.use("ggplot")

proton_mass = 1.672621898e-27             #[kg]
proton_charge = 1.6021766208e-19                 #[C]
valley_gap = 90e-6                      #[m]
E0 = 25000/(90e-6)                      #[V/m]
magnetic_field = np.array([0, 0, 2])
cyclotron_frequency = proton_charge * np.linalg.norm(magnetic_field)/(proton_mass)
r_D = 0.05


total_time = 300e-9
dt = 100e-15
total_time_steps = int(total_time/dt)

positions = np.zeros((3, total_time_steps))
velocities = np.zeros((3, total_time_steps))

def electric_field(x, t):
    if np.absolute(x) <= valley_gap/2:
        return np.array([E0 * np.cos(cyclotron_frequency * t), 0, 0])
    else:
        return np.array([0, 0, 0])

def euler_cromer():
    for t in range(total_time_steps-1):
        force = proton_charge*electric_field(positions[0, t], t*dt) + proton_charge * np.cross(velocities[:, t], magnetic_field)
        acceleration = force / proton_mass

        #Hvis protonet er utenfor skal det ikke akselereres mer.
        if np.linalg.norm(positions[:, t]) >= r_D:
            acceleration = np.array([0, 0, 0])

        velocities[:, t+1] = velocities[:, t] + acceleration*dt
        positions[:, t+1] = positions[:, t] + velocities[:, t+1]*dt


    return positions
def leapfrog():
    for t in range(total_time_steps-1):
        force = proton_charge * electric_field(positions[0, t], t * dt) + proton_charge * np.cross(velocities[:, t], magnetic_field)
        acceleration0 = force / proton_mass

        positions[:, t+1] = positions[:, t] + velocities[:, t]*dt + 0.5*acceleration0*dt**2
        force = proton_charge * electric_field(positions[0, t+1], t * dt) + proton_charge * np.cross(velocities[:, t+1], magnetic_field)
        acceleration1 = force / proton_mass
        velocities[:, t+1] = velocities[:, t] + 0.5*(acceleration0 + acceleration1)*dt

def plot2d(positions):
    time = np.linspace(0, total_time-dt, total_time_steps)

    plt.plot(positions[0, :], positions[1, :])

    w1 = Wedge((valley_gap/2, 0), r_D - valley_gap/2, 270, 450, facecolor="#fdf6f6", edgecolor="Black", linewidth=1)
    w2 = Wedge((-valley_gap/2, 0), r_D - valley_gap/2, 90, 270, facecolor="#fdf6f6", edgecolor="Black", linewidth=1)
    ax = plt.gca()
    ax.add_artist(w1)
    ax.add_artist(w2)

    plt.axis("equal")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend(["position"])
    #plt.savefig("cyclotron_1.png")

    plt.show()

def plot2d_components(positions):
    time = np.linspace(0, total_time-total_time/len(positions[0, :]), len(positions[0, :]))

    plt.plot(time, positions[0, :], time, positions[1, :], time, positions[2, :])

    plt.xlabel("time[s]")
    plt.ylabel("position[m]")

    plt.legend(["x(t)", "y(t)", "z(t)"])

    plt.tight_layout()
    #plt.savefig("cyclotron_3.png")
    plt.show()


plot2d(euler_cromer())
print np.linalg.norm(velocities[:, -1])