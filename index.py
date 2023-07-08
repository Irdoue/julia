import numpy as np
import matplotlib.pyplot as plt
import random
import copy
d = 3
def approx(z, d):
    return complex(round(z.real, d), round(z.imag, d))

# n the rank
# z the first term
# c the constant
def make_progression(n, z, c):
    for i in range(n):
        if modulus(z) >= 2:
            return 1
        z = z**2 + c
        z = approx(z, d)
    return z

def modulus(z):
    return approx((z.real**2 + z.imag**2)**(1/2), d).real

def show_julia(julia):  
    plt.imshow(julia)
    
# n the rank
# c the constant
def make_julia(n, c):
    julia = []
    temp = []
    for l in np.linspace(-2, 2, 4 * 10**2 + 1):
        for k in np.linspace(-2, 2, 4 * 10**2 + 1):
            temp.append(modulus(make_progression(n, complex(k, l), c)))
        julia.insert(0, temp)
        temp = []
    return julia

def make_step(z, c):
    if modulus(z) >= 2:
        return 1
    z = z**2 + c
    z = approx(z, d)
    return z

def make_plan(n):
    plan = []
    temp = []
    for l in np.linspace(-2, 2, 4 * 10**n + 1):
        for k in np.linspace(-2, 2, 4 * 10**n + 1):
            temp.append(approx(complex(k, l), d))
        plan.insert(0, temp)
        temp = []
    return plan

def make_julia_step(plan, c):
    temp = copy.deepcopy(plan)
    for l in range(len(temp)):
        for k in range(len(temp)):
            temp[l][k] = make_step(temp[l][k], c)
    return temp

def show_plan(plan):
    temp = copy.deepcopy(plan)
    for l in range(len(temp)):
        for k in range(len(temp)):
            temp[l][k] = modulus(plan[l][k])
    plt.figure(figsize=(10,10))
    plt.imshow(temp)
    plt.show()
    
plan = make_plan(2)
c = 0.25+0.5j
show_plan(plan)
for i in range(100):
    plan = make_julia_step(plan, c)
    show_plan(plan)