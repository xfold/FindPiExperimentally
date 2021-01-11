# FindPiExperimentally
This is a simple repository to find pi experimentally by generating random points in a plane and comparing the areas of a square and a circle. 

# Procedure
To do so we will generate random points in a 2x2 square, and then compare the areas of the square with
that of the circle to find pi. (we use a 2x2 square so the radius of the circle is 1, therefore simplifying the equations of the area of the circle).

Find pi by comparing the areas of a square and a circle:
<ul>
   <li>a(square) = side²</li>
   <li>a(circle) = pi*r²</li>
</ul>
Considering r = 1:
<ul>
   <li>a(square) = (1*2)² = 4</li>
   <li>a(circle) = 1² * pi = pi</li>
</ul>

Following:
1) Randomly generate points (x,y) that fall within the limits 0<=x<=2
2) Count how many points falls within the square area (all of them) and how many fall within the circle area 
(distance to the center of the circle at (1,1) <= 1
3) Compare the proportion of points that fall within the circle and the square, knowing that the points within the circle are pi/4 times the points inside the square. With this, solve pi (see below)
4) pi = 4*points_inside_circle/points_outside_circle

# Execution
>python FindPy.py 1000000

Where 1000000 is the quantity of random points generated. The more random points generated the more accurate pi.
