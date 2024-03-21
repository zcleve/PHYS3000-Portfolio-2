# Zackary Cleveland PHYS3000

import numpy as np
from numpy import sin , cos


def theta_dot(omega1 , omega2) :
    return np.array([omega1 , omega2])


def omega_dot(omega1 , omega2 , theta1 , theta2 , g = 9.81 , l = 40) :
    om12 = omega1 ** 2
    om22 = omega2 ** 2
    theta_diff = theta1 - theta2
    gl = g / l
    omd1 = ((-om12 * sin(2 * theta1 - 2 * theta2)) + (2 * om22 * sin(theta_diff)) + (
            gl * (sin(theta1 - 2 * theta2) + 3 * sin(theta1)))) / (3 - cos(2 * theta1 - (2 * theta2)))

    omd2 = ((4 * om12 * sin(theta_diff)) + (om22 * sin(2 * theta1 - 2 * theta2)) + (
            2 * gl * (sin(2 * theta1 - theta2) - sin(theta2)))) / (3 - cos(2 * theta1 - (2 * theta2)))
    return np.array([omd1 , omd2])


def rk4_iterator(V , g = 0.81 , l = 40) :
    theta1 = V[0]
    theta2 = V[1]
    omega1 = V[2]
    omega2 = V[3]

    thd = theta_dot(omega1 , omega2)
    omd = omega_dot(omega1 , omega2 , theta1 , theta2 , g , l)
    output = np.zeros(V.shape)
    output[0] = thd[0]
    output[1] = thd[1]
    output[2] = omd[0]
    output[3] = omd[1]
    return output
