# lorenz.py: The Lorenz chaotic attractor in interactive 3D.
#            Note the use of the Euler integration method.

from enthought.mayavi.mlab import axes,plot3d
from numpy import arange

print """
	Rotate: Left-click & drag
	Zoom:   Right-Click & slide up/down
	Slide:  Middle-Click & drag
"""

  # Integration time step
dt = 0.001
  # Lorenz ODE parameters
sigma = 10.0
r     = 28.0
b     = 8.0/3.0
  # Initial conditions
x = -.5
y =  .2
z =  2.17
  # Store the trajectory
TrajX = []
TrajY = []
TrajZ = []
Time  = []

  # Integrate the Lorenz ODEs
  #
for t in arange(0.,250.,dt):
	dxdt = sigma*(y - x)
	dydt = r * x - y - x * z
	dzdt = x * y - b * z
	x = x + dxdt * dt
	y = y + dydt * dt
	z = z + dzdt * dt

	TrajX.append(x)
	TrajY.append(y)
	TrajZ.append(z)
	Time.append(t)

plot3d(TrajX,TrajY,TrajZ,Time,colormap='Spectral',tube_radius=0.1)
axes(color=(0.,0.,0.),extent=[-15.0,15.0,-15.0,15.0,0.0,50.0],ranges=[-15.0,15.0,-15.0,15.0,0.0,50.0])