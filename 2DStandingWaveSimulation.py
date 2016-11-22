#The following code sample simulates a two dimensional standing wave.

#Import the libraries needed to perform the simulation, including numpy, matplotlib for plotting
#animation and mplot3D for 3D plots.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from mpl_toolkits.mplot3d import Axes3D

#Set up the position and time grids (or axes).
axis_size = 100                                                   #Number of points for each grid dimension.
side_length =  5                                                  #Length of one side of one of the wave plot axes.
axis_points = np.linspace(-side_length,side_length,axis_size)     #Spatial grid points

#Set up the time grid to calcuate the equation.
T =  30                                                   #Total time (s)
dt = 0.1                                                  #Time step size
n = int(T/dt)                                             #Total number of time steps

#Create a meshgrid to calculate and plot the 2D standing wave.
X, Y = np.meshgrid(axis_points, axis_points)

#Initialize a 3D array to store each time instance of the standing wave.
map_array = np.zeros((axis_size,axis_size,n))

#Numerically solve the PDE by iteration over the specified total time.
for i in range(n):

    #Calculate an instance of the 2D standing wave, which has a time dependence as well.
    U1 = np.sin(np.pi*X/side_length)*np.sin(np.pi*Y/side_length)*np.cos((2*i*dt))

    #Update the wave array with the current standing wave data.
    map_array[:,:,i] = U1

#Create a movie frame array to store each time instance of the standing wave to be animated.  In this case,
#it is the same size as the original data storage array, but it can be changed.
movie_frames = map_array[:,:,0::1]

#Set up the plot template to animate the wave amplitude changes
#over time.  An initial figure needs to be generated along with the colormap plot
#and the associated labels and axes.
fig = plt.figure()

#Create a 3D projection view for the surface plot.
ax = fig.gca(projection = '3d')

#Generate an initial surface plot using initial standing wave at timepoint t = 0.  Set the grid size for plotting,
#colormap, range and mesh linewidth.
surf = (ax.plot_surface(X,Y,movie_frames[:,:,0], rstride=2, cstride=2,
                        cmap ='RdPu', vmax = np.max(movie_frames), vmin = np.min(movie_frames), linewidth=1))

#Title of plot.
ax.set_title('3D function')

#Add a colorbar to the plot.
fig.colorbar(surf)                         #Add a colorbar to the plot
ax.view_init(elev=30,azim=70)              #Elevation & angle initial view
ax.dist=8                                  #Viewing distance

#Axis limits and labels.
ax.set_xlim3d([-side_length, side_length])
ax.set_xlabel('X')

ax.set_ylim3d([-side_length, side_length])
ax.set_ylabel('Y')

ax.set_zlim3d([np.min(movie_frames),np.max(movie_frames)])
ax.set_zlabel('Z')

#Define the animation update function.  In this function, each standing wave plot will
#be updated with the current frame.
def animate(i):
    ax.clear()
    surf = (ax.plot_surface(X,Y,map_array[:,:,i], rstride=2, cstride=2,
                        cmap ='RdPu', vmax = np.max(movie_frames), vmin = np.min(movie_frames), linewidth=1))

    ax.view_init(elev=30,azim=70)              #Elevation & angle initial view
    ax.dist=8                                  #Viewing distance

    #Axis limits and labels.
    ax.set_xlim3d([-side_length, side_length])
    ax.set_xlabel('X')

    ax.set_ylim3d([-side_length, side_length])
    ax.set_ylabel('Y')

    ax.set_zlim3d([np.min(movie_frames),np.max(movie_frames)])
    ax.set_zlabel('Z')
    ax.set_title('3D function')

    return surf

#Call the full animation function.  The number of frames is given by the last element of the shape tuple of
#of the movie frames array.
anim = animation.FuncAnimation(fig, animate, frames = movie_frames.shape[2])

#Save the animation as an avi movie file to be played at 15 frames per second.
anim.save('wave_animation.avi', fps = 15)

#Display the resulting animated wave map, which shows how wave amplitude changes over time.
plt.show()