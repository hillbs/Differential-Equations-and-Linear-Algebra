# -*- coding: utf-8 -*-
from pylab import *
# Set limits and number of points in grid
xmax = 10.0
xmin = -10
NX = 10
ymax = 10
ymin = -10
NY = 10
# Make grid and calculate vector components
x = linspace(xmin, xmax, NX)
y = linspace(ymin, ymax, NY)
X, Y = meshgrid(x, y)
S2 = X**2 + Y**2  # This is the radius squared
Bx = X
By = Y
figure()
QP = quiver(X,Y,Bx,By)
quiverkey(QP, 0.85, 1.05, 1.0, '1 mT', labelpos='N')
# Set the left, right, bottom, top limits of axes
dx = (xmax - xmin)/(NX - 1) # One less gap than points
dy = (ymax - ymin)/(NY - 1)
axis([xmin-dx, xmax+dx, ymin-dy, ymax+dy])
title('Magnetic Field of a Wire with I=50 A')
xlabel('x (cm)')
ylabel('y (cm)')
show()