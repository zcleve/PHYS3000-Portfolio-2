# Zackary Cleveland PHYS3000
import matplotlib.pyplot as plt
import numpy as np
from vacuumDecayEqns import *


def find_minima(first_guess , first_deriv , second_deriv , tolerance , n_iter = 1000) :
    phi = first_guess
    for i in range(n_iter) :
        fprime = first_deriv(phi)
        f2prime = second_deriv(phi)
        phi = phi - (fprime / f2prime)
        if abs(fprime) < tolerance :
            break
    return phi


phidot_guess = [.01 , 10]
guess = [-1.8 , 1.8]
phi_zeros = []
vacuum_vs = []

for i in guess :
    phi_zeros.append(find_minima(i , dV_dPhi , d2V_dPhi , tolerance = 1e-7))
for i in phi_zeros :
    vacuum_vs.append(V_potential(i))

print('The false vacuum has a potential of ' , max(vacuum_vs) , 'at phi of' , min(phi_zeros))
print('The  vacuum has a potential of ' , min(vacuum_vs) , 'at phi of' , max(phi_zeros))

r_init , phi_init = 1.0 , min(phi_zeros)


def second_order_solver(func , initial_phidot , initial_phi , tf , target , dt = 0.001) :
    steps = int(tf / dt)
    O = np.zeros((3 , steps))  # Array to hold phidotdot, phidot, and phi
    O[1 , 0] = initial_phidot  # Initial phi dot
    O[2 , 0] = initial_phi
    for i in range(1 , steps) :
        O[0 , i - 1] = func(i * dt , O[2 , i - 1] , O[1 , i - 1])  # Phi dot dot
        O[1 , i] = O[1 , i - 1] + O[0 , i - 1] * dt  # Phi dot
        O[2 , i] = O[2 , i - 1] + O[1 , i - 1] * dt  # Phi

        if O[2 , i] >= target :
            break

    final_phi = O[2 , i]
    return final_phi , O[1 , i]


v1 , v2 = phidot_guess
tolerance = 1e-7
d = max(phi_zeros)
while abs(v1 - v2) > tolerance :
    v_next = (v1 + v2) / 2
    final_phi , final_phidot = second_order_solver(phi_2dot , v_next , min(phi_zeros) , 1 , d)
    if final_phi < d :
        v1 = v_next
    else :
        v2 = v_next

v_final = (v1 + v2) / 2
print('The necessary phi-dot is:',v_final)

