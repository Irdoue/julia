import numpy as np
import matplotlib.pyplot as plt
import random
import copy

def modulus(z):
    """
    Return the modulus of a complex.

    :param z: A complex.
    :type z: complex
    :return: The modulus of z.
    :rtype: float

    """
    if z == None:
        return None
    return (z.real**2 + z.imag**2)**(1/2).real

def make_step(z, c):
    """
    Return the next step of the c-julia progression for a complex z.

    :param z: The actual term of the c-julia progression.
    :type z: complex
    :param c: The associated constant of the Julia's progression.
    :type c: complex
    :return: The next term of the c-julia progression.
    :rtype: complex or None

    """
    if z != None:
        z = z**2 + c
    return z

def make_plan(decimal):
    """
    Return the plan of complex.

    :param decimal: The number of decimal in each complex.
    :type decimal: int
    :return: The plan of complex with the selected number of decimal.
    :rtype: list[list[complex]]

    """
    plan = []
    temp = []
    for l in np.linspace(-2, 2, 4 * 10**decimal + 1):
        for k in np.linspace(-2, 2, 4 * 10**decimal + 1):
            temp.append(complex(k, l))
        plan.insert(0, temp)
        temp = []
    return plan

def make_julia_step(julia, c):
    """
    Return the next step of an actual c-julia step.

    :param julia: The actual Julia's trail.
    :type julia: list[list[complex]]
    :param c: The associated Julia's constant.
    :type c: complex
    :return: A matrice of complex representing the Julia's set.
    :rtype: list[list[complex]]

    """
    temp = copy.deepcopy(julia)
    for l in range(len(temp)):
        for k in range(len(temp)):
            temp[l][k] = make_step(temp[l][k], c)
            if temp[l][k] == None or modulus(temp[l][k]) >= 2:
                temp[l][k] = None
    return temp

def save_plan(julia, name):
    """
    Make and save the Julia's set with a specified name in ./pictures/ .

    :param julia: A Julia's trail.
    :type julia: list[list[complex]]
    :param name: The name of the saved picture.
    :type name: str

    """
    temp = copy.deepcopy(julia)
    for l in range(len(temp)):
        for k in range(len(temp)):
            if temp[l][k] == None:
                temp[l][k] = 0
            else:
                temp[l][k] = modulus(julia[l][k])
    plt.figure(figsize=(19,19))
    img = plt.imshow(temp)
    plt.axis('off')
    #plt.show()
    #plt.savefig('./pictures/' + name, bbox_inches = 'tight', pad_inches = 0.0)
    #envoie à 
    plt.close()

# Some nice constants.

#c = 0.25+0.5j
#c = -0.5251993
#c = 0.285 + 0.01j
#c = -0.7269 + 0.1889j
#c = 0.7885
c = 0.28+0.008j

c_random = complex(4 * random.random() - 2, 4 * random.random() - 2)

def main(plan, c):
    save_plan(make_julia_step(plan, c), user_ID)
    