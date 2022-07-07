''' 
height = y(t) = hs + (t * v * sin(a)) - (g * t*t)/2
distance = x(t) = v * cos(a) * t

t = time in seconds
v = muzzle velocity (meters/second)
a = firing angle (radians)
hs = starting height (meters)
g = gravitational pull (meters/second_square)

'''

import math

# This function returns a list containing vector coordinates that represent the trajectory that a projectile would take given the selected inputs.

def projectile_xy(v, a, hs=0.0, g=9.8):
    data_xy = []
    t = 0.0
    d = a
    a = math.radians(d)
    while True:
        # now calculate the height y
        y = hs + (t * v * math.sin(a)) - (g * t * t)/2
        # projectile has hit ground level
        if y < -100:
            break
        # calculate the distance x
        x = v * math.cos(a) * t
        # append the (x, y) tuple to the list
        y -= y*2
        x -= x*2
        data_xy.append((int(x), int(y)))
        # use the time-step of 0.1 seconds
        t += 0.1
    return data_xy


# This function returns the final x coordinate in the list of tuples generated above.

def giveFinalX(v, a, hs=0.0, g=9.8):
    data_xy = []
    t = 0.0
    d = a
    a = math.radians(d)
    while True:
        y = hs + (t * v * math.sin(a)) - (g * t * t)/2
        if y < -20:
            return x
            break
        x = v * math.cos(a) * t
        y -= y*2
        x -= x*2
        t += 0.1

# This function returns the initial velocity of a projectile in motion given an angle, angle in radians and time.

def initial_vel_calc(a,d,t,hs=0.0,g=9.8):
    ut = (1/2)*(a*t)**2+d
    return ut




