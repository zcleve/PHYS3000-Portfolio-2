import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import patches
import rk4_v1
import pendulumEqns as peqns

PI = np.pi
V0 = np.array([PI / 2 , PI / 2 , 0 , 0])
steps = 1000
tf = 30
variable_space , t_space = rk4_v1.runge_kutta_coupled(peqns.rk4_iterator , V0 , tf, 0 , n_iter=steps)
print(t_space.size)

theta_over_t = variable_space[:2 , :]
cx , cy = 0 , 1

fig , ax = plt.subplots()

# Initialize plot elements
ax.set_xlim(-1 , 1)
ax.set_ylim(-1 , 2)
ax.set_aspect('equal')

# Create and add pendulum bob and rod as patches and lines
bob1 = patches.Circle((0 , 0) , 0.05 , color = 'red')
bob2 = patches.Circle((0 , 0) , 0.05 , color = 'blue')
ax.add_patch(bob1)
ax.add_patch(bob2)
line1 , = ax.plot([] , [] , 'black' , lw = 2)
line2 , = ax.plot([] , [] , 'black' , lw = 2)

vtime_text = ax.text(0.05 , 0.9 , '' , transform = ax.transAxes)
time_text = ax.text(0.05 , 0.8 , '' , transform = ax.transAxes)

def update(frame) :
    x = cx + (.40 * np.sin(theta_over_t[0 , frame]))
    y = cy + (.40 * np.cos(theta_over_t[0 , frame]))
    x2 = x + (.40 * np.sin(theta_over_t[1 , frame]))
    y2 = y - (.40 * np.cos(theta_over_t[1 , frame]))

    bob1.center = (x , y)
    bob2.center = (x2 , y2)

    line1.set_data([cx , x] , [cy , y])
    line2.set_data([x , x2] , [y , y2])
    vtime_text.set_text('virtual time = %.1fs' % (frame * tf / steps))

    return bob1 , bob2 , line1 , line2 , vtime_text, time_text
fps = 200
delay = 1000/fps
ani = FuncAnimation(fig , update , frames = len(t_space) ,
                    blit = True , interval = delay, repeat_delay = 1000)  #

plt.show()