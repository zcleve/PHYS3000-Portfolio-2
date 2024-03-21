# Zackary Cleveland PHYS3000
import numpy as np
from vacuumDecayEqns import *


# Finds the minima using the gradient descent method
def find_minima(first_guess , first_deriv , second_deriv , tolerance , n_iter = 1000) :
    phi = first_guess
    for i in range(n_iter) :
        fprime = first_deriv(phi)
        f2prime = second_deriv(phi)
        phi = phi - (fprime / f2prime) # works by using the signs and magnitudes of the first and second derivatives to move left and right of the minima until reaching within the tolerance
        if abs(fprime) < tolerance :
            break
    return phi


phidot_guess = [.01 , 10]  # initial guesses for phidot for the shooting method, arbitraily chosen and happened to work
guess = [-1.8 , 1.8]  # initial guesses near the left and right bounds to find both minima
phi_zeros = []
vacuum_vs = []

for i in guess :
    phi_zeros.append(find_minima(i , dV_dPhi , d2V_dPhi , tolerance = 1e-7))  # finds the phi value of the zeros
for i in phi_zeros :
    vacuum_vs.append(V_potential(i))  # gets the potential at the phi zeros

print('The false vacuum has a potential of ' , max(vacuum_vs) , 'at phi of' , min(phi_zeros))
print('The  vacuum has a potential of ' , min(vacuum_vs) , 'at phi of' , max(phi_zeros))

r_init , phi_init = 1.0 , min(phi_zeros)  # r_init is unused.


# performs close to euler's method with a very low step size to ensure accuracy
def second_order_solver(func , initial_phidot , initial_phi , tf , target , dt = 0.00001) :
    steps = int(tf / dt)
    O = np.zeros((3 , steps))  # Array to hold phidotdot, phidot, and phi
    O[1 , 0] = initial_phidot  # Initial phi dot
    O[2 , 0] = initial_phi
    for i in range(1 , steps) :
        O[0 , i - 1] = func(i * dt , O[2 , i - 1] , O[1 , i - 1])  # Phi dot dot. Note that i * dt is used to facilitate the domain change of (1,inf) to (0,1)
        O[1 , i] = O[1 , i - 1] + O[0 , i - 1] * dt  # Phi dot
        O[2 , i] = O[2 , i - 1] + O[1 , i - 1] * dt  # Phi

        if O[2 , i] >= target :  # stops when we reach phi of the true vacuum to save on time
            break

    final_phi = O[2 , i]
    return final_phi , O[1 , i]  # returns the last value of phi and the corresponding phi_dot of the iteration for
    # the shooting method below


v1 , v2 = phidot_guess  # holds the two initial guesses of phi_dot
tolerance = 1e-7  # tolerance for equality to the expected value of phi
d = max(phi_zeros)  # grabs the phi of the true vacuum
while abs(
        v1 - v2) > tolerance :  # iterates the shooting method, changing the value of phi_dot each time until the
    # true vacuum is reached when r -> infinity
    v_next = (v1 + v2) / 2
    final_phi , final_phidot = second_order_solver(phi_2dot , v_next , min(phi_zeros) , 1 , d)
    if final_phi < d :
        v1 = v_next
    else :
        v2 = v_next

v_final = (v1 + v2) / 2
print('The necessary phi-dot is:' , v_final)
