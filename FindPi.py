#
# FindPi
# xfold, Jan 2021
#
# To do so we will generate random points in a 2*2 square, and then compare the areas of the square with
# that of the circle to find pi. (we use a 2*2 square so the radius of the circle is 1, therefore simplifying the
# equations of the area of the circle)
#
# Find pi by comparing the areas of a square and a circle
#    a(square) = side²
#    a(circle) = pi*r²
# Considering r = 1-->
#    a(square) = (1*2)² = 4
#    a(circle) = 1² * pi = pi
# 
# Following:
# 1) Randomly generate points (x,y) that fall within the limits 0<=x<=2
# 2) Count how many points falls within the square area (all of them) and how many fall within the circle area 
# (distance to the center of the circle at (1,1) <= 1
# 3) Compare the proportion of points that fall within the circle and the square, knowing that the points within the circle are pi/4 times the points inside the square. With this, solve pi (see below)
# 
# Regla de tres
# points_inside_circle       pi
# points_outside_circle      4
# 
# pi = 4*points_inside_circle/points_outside_circle

import matplotlib
from matplotlib import pyplot as plt
import random
import sys

#change this value for more precision, the more random points generated the more
#precisely will pi be described
randompoints = 100000


def GetRandomPoint():
    '''
    returns a random point within the range (0<=x<=2, 0<=y<=2)
    '''
    return (random.uniform(0, 2), random.uniform(0, 2))
    

def PrintPoints(pointList):
    '''
    Creates and prints a scatter plot to print a list of points,:
        pointList : [(p1x, p1y), (p2x, p2y), ..., (pnx, pny)]
    '''
    fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1) 
    ax.set_xlabel('X', fontsize = 15)
    ax.set_ylabel('Y', fontsize = 15)
    ax.set_title('Generated Points Plot', fontsize = 20)
    ax.scatter([x[0] for x in pointList], 
               [x[1] for x in pointList], 
               s = 10)
    ax.grid()

def GetPointsInsideRadius(allpoints, radius=1, origin=(1,1)):
    '''
    Counts how many points from allpoints fall within 'radius' of the circle with center 'origin'
    '''
    pointsinside= []
    for p in allpoints:
        distancetocenter = ((origin[0]-p[0])**2 + (origin[1]-p[1])**2 )**0.5
        if(distancetocenter <= radius):
            pointsinside.append(p)
    return pointsinside

#parse args (if any)
if(len(sys.argv)>1):
    try:
        randompoints = int(sys.argv[1])
    except Exception as e:
        print('Parameter 1:', sys.argv[1], 'should be an integerm using 100000 random points...')
print('Generating', randompoints, 'random points...')
    
#Generate random points
allpoints = []
for k in range(randompoints):
    allpoints.append(GetRandomPoint())

#select points inside circle
pointsInside = GetPointsInsideRadius(allpoints)

#estimate pi, since the points inside the circle should be proportional to 
#pi and the points inside the square proportional to 4, we can determine pi by 
#dividing the number of points inside the circle by the total points in the square and multiply it by 4
pi = (len(pointsInside)*4) / len(allpoints)
print('Total Points', len(allpoints))
print('Points inside circle', len(pointsInside))
print('Pi value', pi)

#print random points scatter plot
PrintPoints(allpoints)
