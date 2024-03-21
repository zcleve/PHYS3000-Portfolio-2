# Zackary Cleveland PHYS3000
import numpy as np
from rungeKatta1ODEv2 import runge_katta_vector
from firstOrderODE_Functionsv2 import vector2D_free_fall
from differentialEqnPlotterv2 import plot_versus_time
from matplotlib import pyplot as plt
from vectorMathv2 import magnitude_over_t
import numericalAnalysisv1 as fna
from numpy.linalg import norm

V0 = np.transpose(np.array([35,20]))
tf = 100
dt = 10000
drag_coeff = 1.225 * (10 ** -3)
m = 0.142
g = 9.81

V_space, t_space = runge_katta_vector(vector2D_free_fall , tf , args=(drag_coeff, m, g) , V_0 = V0 , t0 = 0 , dt = dt)
u_space = V_space[0,:]
v_space = V_space[1,:]
V_norm = magnitude_over_t(V_space , n_dimn = 2)

fig, ax = plt.subplots(1, 2, figsize=(12,7.2))
fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.2, hspace=None)

plot_versus_time(ax[0],t_space[0,:],u_space,"X Velocity vs Time in seconds", y_label ='u(t)', f_label ='Horizontal Velocity')

plot_versus_time(ax[1],t_space[0,:],v_space,"Y Velocity vs Time in seconds", y_label ='v(t)', f_label ='Veritcal Velocity')

fig2, ax2 = plt.subplots()
plot_versus_time(ax2,t_space[0,:],V_norm,"Velocity Magnitude vs Time in seconds", f_label ='Velocity magnitude')
plot_versus_time(ax2,t_space[0,:],np.repeat(V_norm[fna.find_asymptotic_index(V_norm, tolerance = 1e-7)],dt+1),"Terminal Speed", f_label ='Terminal Speed', color = 'blue')


plt.show()
