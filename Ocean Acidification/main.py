# Zackary Cleveland PHYS3000
import eqns as eq
import numpy as np
import differentialEqnPlotterv2 as deplt
import matplotlib.pyplot as plt
from tqdm import tqdm


def runge_katta_coupled(coupled_funcs , inital_state , tf , ti , dt = 100 , non_de_starting_index = 0) :
    num_steps = ((tf - ti) * dt)

    x_space = np.zeros((inital_state.size , num_steps+1))  # Creates placeholder output space for dependent variables
    x_space[: , 0] = inital_state  # Applies IVP condition
    t_space = np.linspace(ti , tf , num = num_steps + 1)  # Assigns the values of t given the final time specified and the time steps plus one bc array index start at 0

    rk = np.zeros(inital_state.size)

    h = (tf - ti) / ((tf - ti) * dt)

    if non_de_starting_index == 0 :
        for i in tqdm(range(num_steps), desc="Simulation Progress"):  # Iterates the runge katta 4th order method across the x,t arrays
            x_iter , t_iter = x_space[: , i] , t_space[i]
            # print(x_iter)
            k1 = h * coupled_funcs(x_iter , t_iter)
            k2 = h * coupled_funcs(x_iter + (1 / 2) * k1 , t_iter + (1 / 2) * h)
            k3 = h * coupled_funcs(x_iter + (1 / 2) * k2 , t_iter + (1 / 2) * h)
            k4 = h * coupled_funcs(x_iter + k3 , t_iter + h)
            rk = (1 / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

            x_space[: , i + 1] = x_iter + rk
    else :
        for i in tqdm(range(num_steps), desc="Simulation Progress"):  # Iterates the runge katta 4th order method across the x,t arrays
            x_iter , t_iter = x_space[: , i] , t_space[i]
            #test = coupled_funcs((x_iter[:non_de_starting_index]),t_iter)
            #print(coupled_funcs((x_iter[:non_de_starting_index]),t_iter))
            k1 = h * coupled_funcs(x_iter[:non_de_starting_index] , t_iter)
            k2 = h * coupled_funcs(x_iter[:non_de_starting_index] + (1 / 2) * k1[:non_de_starting_index] , t_iter + (1 / 2) * h)
            k3 = h * coupled_funcs(x_iter[:non_de_starting_index] + (1 / 2) * k2[:non_de_starting_index] , t_iter + (1 / 2) * h)
            k4 = h * coupled_funcs(x_iter[:non_de_starting_index] + k3[:non_de_starting_index] , t_iter + h)
            rk[:non_de_starting_index] = (1 / 6) * (k1[:non_de_starting_index] + 2 * k2[:non_de_starting_index] + 2 * k3[:non_de_starting_index] + k4[:non_de_starting_index])

            x_space[:non_de_starting_index , i + 1] = x_iter[:non_de_starting_index] + rk[:non_de_starting_index]

            os , alpha_s = x_space[1 , i + 1] , x_space[3 , i + 1]
            x_space[5 , i + 1] = eq.hs_func(os , alpha_s)
            x_space[6 , i + 1] = eq.cs_func(os , alpha_s)
            x_space[7 , i + 1] = eq.ps_func(os , alpha_s)

    return x_space , t_space


variable_space , t_space = runge_katta_coupled(eq.runge_katta_iterator , eq.init_array(5000 , 1000)[: , 0] , 5000 ,
                                               1001 , dt = 10 , non_de_starting_index = 5)

fig , ax = plt.subplots()

deplt.plot_versus_time(ax , t_space , variable_space[0 , :] , 'Ocean Acidification over Time' , color = "red" , f_label = 'P')
deplt.plot_versus_time(ax , t_space , variable_space[1 , :] , 'Ocean Acidification over Time' , color = "green" , f_label = 'os')
deplt.plot_versus_time(ax , t_space , variable_space[2 , :] , 'Ocean Acidification over Time' , color = "blue" , f_label = 'od')
deplt.plot_versus_time(ax , t_space , variable_space[3 , :] , 'Ocean Acidification over Time' , color = "yellow" , f_label = 'alpha_s')
deplt.plot_versus_time(ax , t_space , variable_space[4 , :] , 'Ocean Acidification over Time' , color = "cyan" , f_label = 'ad')
deplt.plot_versus_time(ax , t_space , variable_space[5 , :] , 'Ocean Acidification over Time' , color = "magenta" , f_label = 'hs')
deplt.plot_versus_time(ax , t_space , variable_space[6 , :] , 'Ocean Acidification over Time' , color = "lime" , f_label = 'cs')
deplt.plot_versus_time(ax , t_space , variable_space[7 , :] , 'Ocean Acidification over Time' , color = "orange" , f_label = 'ps')
plt.show()
