import numpy as np

def calc_pi():
    # function that calculates pi
    a = 3.14
    return a

print(calc_pi())

def calc_pi_monte_carlo():
    n = 10000000000 # number of points to generate
    count = 0 # counter for points inside the circle
    for i in range(n):
        x = np.random.uniform(-1, 1) # random x coordinate between -1 and 1
        y = np.random.uniform(-1, 1) # random y coordinate between -1 and 1
        if x**2 + y**2 <= 1: # check if point is inside the circle
            count += 1
    pi_approx = 4 * count / n # calculate approximation of pi
    return pi_approx

print(calc_pi_monte_carlo())

def calc_pi_leibniz():
    n = 10000000000 # number of terms to sum
    pi_approx = 0 # initialize approximation of pi
    for i in range(n):
        term = (-1)**i / (2*i + 1) # calculate next term in the series
        pi_approx += term # add term to the sum
        π = pi_approx * 4 # multiply by 4 to get approximation of pi
        π = round(π, 6) # round to 6 decimal places
        π = str(π) # convert to string for output formatting
        π = π[:1] + "." + π[1:] # add decimal point for output formatting
        π = π.replace(".", ". ", 1) # add space after decimal point for output formatting
    return π

print(calc_pi_leibniz())


