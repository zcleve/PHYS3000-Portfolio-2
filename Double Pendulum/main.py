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
variable_space , t_space = rk4_v1.runge_kutta_coupled(peqns.rk4_iterator , V0 , tf , 0 ,
                                                      n_iter = steps)  # generates the time and variable space for
# the differential equation with the specified starting  conditions and time domain


theta_over_t = variable_space[:2 , :]
cx , cy = 0 , 1  # pin location for first pendulum

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


def update(frame) :
    # basic trig using the given length of the pendulum rope and their angles to determine bob coordinates
    x = cx + (.40 * np.sin(theta_over_t[0 , frame]))
    y = cy + (.40 * np.cos(theta_over_t[0 , frame]))
    x2 = x + (.40 * np.sin(theta_over_t[1 , frame]))
    y2 = y - (.40 * np.cos(theta_over_t[1 , frame]))

    # resets the centers of each bob each update
    bob1.center = (x , y)
    bob2.center = (x2 , y2)

    # connects the lines for the first and second pendulum
    line1.set_data([cx , x] , [cy , y])
    line2.set_data([x , x2] , [y , y2])

    # keeps track of the virtual time
    vtime_text.set_text('virtual time = %.1fs' % (frame * tf / steps))

    return bob1 , bob2 , line1 , line2 , vtime_text


fps = 400  # unreliable used to set frame rates, I've gotten this to do 1000fps, but sometimes it refuses to go
# beyond around 400 (meaning it just doesn't speed up since the update time exceeds the desired frame update time)
# redrawing in matplotlib is pretty inefficient for animation, so I will explore how to do that better in the future
delay = 1000 / fps  # interval takes in a delay in ms this calculates the delay for a given frame rate
ani = FuncAnimation(fig , update , frames = len(t_space) ,
                    blit = False , interval = delay , repeat_delay = 1000)  #

plt.show()
