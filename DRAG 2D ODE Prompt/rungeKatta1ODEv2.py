import numpy as np


def runge_kutta(func , x0 , tf , args = () , t0 = 0 , dt = 1000) :
    """
       Solve first-order ordinary differential equations (ODEs) using the Runge-Kutta method.

       Parameters:
       - func: Function representing the first-order ODE.
       - x0: Initial value of the dependent variable.
       - tf: Final time.
       - args: Additional arguments to be passed to the function.
       - t0: Initial time (default is 0).
       - dt: Number of time steps (default is 1000).

       Returns:
       - x_space: NumPy array containing the numerically approximated values of the dependent variable over time.
       - t_space: NumPy array containing the time values.
    """

    x_space = np.zeros(
        dt + 1)  # Creates an array to hold all the future calculated values of 'x' based on the time steps argument
    x_space[0] = x0  # Applies the initial value condition

    t_space = np.linspace(t0 , tf ,
                          num = dt + 1)  # Generates the values of t given the final time specified and the time steps plus one bc array index start at 0
    h = (tf - t0) / dt  # Creates the runge katta step size

    for i in range(dt) :  # Iterates the runge katta 4th order method across the x,t arrays
        x_iter , t_iter = x_space[i] , t_space[i]
        k1 = h * func(x_iter , t_iter , *args)
        k2 = h * func(x_iter + (1 / 2) * k1 , t_iter + (1 / 2) * h , *args)
        k3 = h * func(x_iter + (1 / 2) * k2 , t_iter + (1 / 2) * h , *args)
        k4 = h * func(x_iter + k3 , t_iter + h , *args)
        rk = (1 / 6) * (k1 * 2 * k2 + 2 * k3 + k4)

        x_space[i + 1] = x_iter + rk
    return x_space , t_space


def runge_katta_vector(F_vector , tf , args = () , V_0 = np.array([0 , 0]) , t0 = 0 , dt = 1000) :
    """
        Solve vector-valued ordinary differential equations (ODEs) using the Runge-Kutta method.

        Parameters:
        - F_vector: Function representing the vector-valued ODE.
        - tf: Final time.
        - args: Additional arguments to be passed to the function.
        - V_0: Initial values of the dependent variables.
        - t0: Initial time (default is 0).
        - dt: Number of time steps (default is 1000).

        Returns:
        - x_space: NumPy array containing the numerically approximated values of the dependent variables over time.
        - t_space: NumPy array containing the time values.
    """

    x_space = np.zeros((V_0.size , dt + 1))  # Creates placeholder output space for dependent variables
    x_space[: , 0] = V_0  # Applies IVP condition

    t_space = np.ones((2 , dt + 1))  # Generates array for t_space of the proper dimensions
    t_space[: , :] = np.linspace(t0 , tf ,
                                 num = dt + 1)  # Assigns the values of t given the final time specified and the time steps plus one bc array index start at 0

    h = (tf - t0) / dt

    for i in range(dt) :  # Iterates the runge katta 4th order method across the x,t arrays
        x_iter , t_iter = x_space[: , i] , t_space[0 , i]
        k1 = h * F_vector(x_iter , t_iter , *args)
        k2 = h * F_vector(x_iter + (1 / 2) * k1 , t_iter + (1 / 2) * h , *args)
        k3 = h * F_vector(x_iter + (1 / 2) * k2 , t_iter + (1 / 2) * h , *args)
        k4 = h * F_vector(x_iter + k3 , t_iter + h , *args)
        rk = (1 / 6) * (k1 * 2 * k2 + 2 * k3 + k4)

        x_space[: , i + 1] = x_iter + rk
    return x_space , t_space
