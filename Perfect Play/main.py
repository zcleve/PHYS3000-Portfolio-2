# Zackary Cleveland PHYS3000

import numpy as np

mu = 0.025
g = 9.81
d = 2.35
tolerance = 1e-6
initial_velocity_guess = [0.1 , 10]  # Lower and upper bounds for the velocity guess
t_f , d_t = 10 , .01


def x_2dot() :
    return -mu * g

#
def second_order_solver(func , initial_velocity , tf , target_distance , dt = 0.01) :
    steps = int(tf / dt)
    O = np.zeros((3 , steps))  # Array to hold acceleration, velocity, and position
    O[1 , 0] = initial_velocity  # Initial velocity
    for i in range(1 , steps) :
        O[0 , i - 1] = func()  # Acceleration
        O[1 , i] = O[1 , i - 1] + O[0 , i - 1] * dt  # Velocity
        O[2 , i] = O[2 , i - 1] + O[1 , i - 1] * dt  # Position

        # Check if we've reached or passed the target distance or if the puck has stopped
        if O[2 , i] >= target_distance or O[1 , i] <= 0 :
            break

    final_position = O[2 , i]
    return final_position , O[1 , i]


# shooting method
v1 , v2 = initial_velocity_guess
while abs(v1 - v2) > tolerance :
    v_next = (v1 + v2) / 2
    final_position , final_velocity = second_order_solver(x_2dot , v_next , t_f , d , dt = d_t)

    if final_position < d :
        v1 = v_next
    else :
        v2 = v_next

v_final = (v1 + v2) / 2

print(v_final)
