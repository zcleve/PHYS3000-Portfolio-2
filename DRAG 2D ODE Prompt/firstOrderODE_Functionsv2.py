import numpy as np
import vectorMathv2 as vm


# example function of returning the output voltage of a lowpass filter consisting of initially a micro-farad
# capacitor and a mega-ohm resistor. Takes both constants and functions for the input signal/voltage.
def f_lpf(f , v , t , r = 1e6 , c = 1e-6 , args = ()) :
    """
        Calculate the output voltage of a crude low-pass filter.

        Parameters:
        - f: Function representing the input signal/voltage.
        - v: Input voltage.
        - t: Time.
        - r: Resistance (default is 1e6).
        - c: Capacitance (default is 1e-6).
        - args: Additional arguments for the input signal function.

        Returns:
        - Output voltage of the low-pass filter.
    """

    tau = c * r
    pi = np.pi
    return f(*args) / tau


# function to return dV/dt in terms of V, i.e. the 1st ODE form of drag
# meant to be used with a numerical ODE solver, i.e. rungeKatta1ODE
# derived from F=−mg+cv^2
def f_free_fall_drag(v , t , c , m , g = 9.81) :
    """
        Calculate dV/dt in terms of V, representing the first-order ODE form of drag.

        Parameters:
        - v: Velocity.
        - t: Time.
        - c: Drag coefficient.
        - m: Mass.
        - g: Gravitational acceleration (default is 9.81).

        Returns:
        - First-order derivative of velocity with respect to time.
    """

    return -g + ((c * v ** 2) / m)


# free fall of an object without drag, a = -g
def f_free_fall(a , b , g = 9.81) :
    """
       Calculate the acceleration of free fall without drag.

       Parameters:
       - a, b: Placeholder parameters (not used).
       - g: Gravitational acceleration (default is 9.81).

       Returns:
       - Acceleration of free fall without drag.
    """

    return -g


def vector2D_free_fall(V_vector , t , c , m , g = 9.81) :
    """
      Calculate the acceleration of free fall with drag in 2D vector form.

      Parameters:
      - V_vector: Velocity vector.
      - t: Time.
      - c: Drag coefficient.
      - m: Mass.
      - g: Gravitational acceleration (default is 9.81).

      Returns:
      - Acceleration vector of free fall with drag.
    """
    g_vec = np.transpose(np.array([0,-g])) # Gravity vector
    return g_vec - ((c * np.linalg.norm(V_vector)) / m)*V_vector
