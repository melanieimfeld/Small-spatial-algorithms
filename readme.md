# Algorithms toolbox


## 1) Conway's Game of Life
## Ramer-Douglas-Peucker Line Simplification


### Step 1) Getting the distance between baseline and furthest point

First, we need to find the function for the baseline, which is defined by:
` y = mx + b `

We can find the slope m by subtracting x_start from x_end and y_start from y_end and dividing the resulting distances:
`m = (x_start - x_end) / (y_start - y_end)`

From that, we'll be able to derive `b`:
b = y - mx


