import math

data = [(0,1),(1,1),(-1,2),(1,2),(3,3)]


print(-2/-1)

def checkDistance(data, point, start_idx, end_idx): 
  # start = data[0]   (a,b)
  start = data[start_idx]    # (x_0, y_0)
  end = data[end_idx-1]     # (x_1, y_1)

  #getting m
  m = (end[1] - start[1]) / (end[0] - start[0])

  # Plug in y, x, m to calculate b    -> y = mx + b -> y - mx = b
  b = start[1] - m * start[0]

  # y = mx + b 
  # ax + by + c= 0   
  # mx + b - y = 0 
  # mx + (-1)y + b = 0 
  a = m 
  b = -1 
  c = b 
  
  d = abs(a * point[0] + b * point[1] + c) / math.sqrt(a**2 + b**2)

  return d
 

def RDP(data, epsilon, start_idx, end_idx): 
  max_id = 0 
  max_dist = 0 

  for i in range(start_idx + 1, end_idx - 1):
    # Need to calculate line using the data array 
    dist = checkDistance(data, data[i], start_idx, end_idx)
    if dist > max_dist: 
      max_id = i 
      max_dist = dist 
    print(f'i: {i} dist: {dist} max_dist: {max_dist} max_id {max_id}')

  if max_dist > epsilon: 
    print(f'Split at: {data[max_id]}')
    RDP(data, epsilon, start_idx=start_idx, end_idx=max_id)
    RDP(data, epsilon, start_idx=max_id, end_idx=end_idx)
  else: 
    # Remove points 
    print(start_idx, end_idx)




RDP(data, 1, 0, len(data))


def checkDistance(data, point, start_idx, end_idx): 
  
##### LINE 1
  # start = data[0]   (a,b)
  start = data[start_idx]    # (x_0, y_0)
  end = data[end_idx-1]     # (x_1, y_1)

  #getting m
  m = (end[1] - start[1]) / (end[0] - start[0])

  # Plug in y, x, m to calculate b    -> y = mx + b -> y - mx = b
  b = start[1] - m * start[0]

  #slope intercept to standard form
  


#### LINE 2
  m2 = -(1/m)

  b = point[0] - m2 * point[1]

### find point on baseline perpendicular
# -------------
  a = m 
  b = -1 
  c = b 
  
  d = abs(a * point[0] + b * point[1] + c) / math.sqrt(a**2 + b**2)

  return d

