# Algorithms toolbox

## Ramer-Douglas-Peucker Line Simplification
### What do we need it for and how does it work?
The Ramer-Douglas-Peucker algorithm is used in cartographic generalization to simplify vector lines, though in any standard GIS software, there will be a command to execute the RDP or a similar algorithm without having to know how it works under the hood. Though it was developed for GIS problems, it can also be applied to computer vision problems, such as simplifying contours.

The function for the algorithm takes in an array of points (i.e. the line we want to simplify) as well as a "threshold" variable, epsilon. The algorithm starts by connecting the first and the last point of the original line with a "baseline". It then finds the point that is furthest away from that baseline. 

If that point is greater than epsilon, it will be kept and the function continues recursively by splitting the line into two segments and repeating the procedure.
If the point is nearer from the baseline than epsilon, then all the points along the baseline can be discarded as they will be smaller than epsilon too. 

The output will be an array containing only those points that were marked as kept. 

### Step 1) Getting the distance between baseline and furthest point `checkdistance()

First, we need to find the function for the baseline, which is defined by:  
` y = mx + b `

We can find the slope m by subtracting x_start from x_end and y_start from y_end and dividing the resulting distances:  
`m = (x_start - x_end) / (y_start - y_end)`

From that, we'll be able to derive `b` by simply plugging in `m`, `x` or `x_start`, and `y` or `y_start`:  
`b = y - mx` -> `b = y_start - m * x_start`

Next, we'll have to transform the slope intercept notation of our baseline to the standard form ax + by + c = 0:  
y = mx + b -> 0 = mx - (1)y - b

Therefore:  
m = a  
b = -1  
c = -b  

We can then use the following formula to get the distance between a line and a point. 
`d = abs(a * x_point - b * y_point + c / sqrt(a^2 + b^2)`


### Step 1) Getting the distance between baseline and furthest point

## Hausdorff Distance between curves
## Rtrees
