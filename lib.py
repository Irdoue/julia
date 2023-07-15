import numpy as np
import matplotlib.pyplot as plt
import random
import copy

# Some nice constants.

#c = 0.25+0.5j
#c = -0.5251993
#c = 0.285 + 0.01j
#c = -0.7269 + 0.1889j
#c = 0.7885
#c = 0.28+0.008j
#c = 0.3 + 0.5j
#c = –1.417022285618 + 0.0099534j
#c = 0.285 + 0.013j
#c = 0.8 + 0.2j
#c = 1
#c = −0.8 + 0,156j

c_random = complex(4 * random.random() - 2, 4 * random.random() - 2)

def modulus(z):
    """
    Return the modulus of a complex.

    :param z: A complex.
    :type z: complex
    :return: The modulus of z.
    :rtype: float

    """
    if z == '_':
        return '_'
    return (z.real**2 + z.imag**2)**(1/2).real

def make_step(z, c):
    """
    Return the next step of the c-julia progression for a complex z.

    :param z: The actual term of the c-julia progression.
    :type z: complex
    :param c: The associated constant of the Julia's progression.
    :type c: complex
    :return: The next term of the c-julia progression.
    :rtype: complex or '_'

    """
    if z != '_':
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

def make_julia_step(julia = make_plan(2), c = c_random):
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
            if temp[l][k] == '_' or modulus(temp[l][k]) >= 2:
                temp[l][k] = '_'
    return temp

def save_pic(julia, name):
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
            if temp[l][k] == '_':
                temp[l][k] = 0
            else:
                temp[l][k] = modulus(julia[l][k])
    plt.figure(figsize=(19,19))
    img = plt.imshow(temp)
    plt.axis('off')
    #plt.show()
    plt.savefig(name, bbox_inches = 'tight', pad_inches = 0.0)
    plt.close()

def file_to_plan(user_ID):
    plan = []
    file = open('/tmp/' + user_ID + '.plan', 'r')
    plan = [e.rstrip().split(';') for e in file]
    for i in plan:
        for j in range(len(i)):
            if i[j] != '_':
                i[j] = complex(i[j])
    return plan
    
def plan_to_file(plan, user_ID):
    file = open('/tmp/' + user_ID + '.plan', 'w')
    for i in plan:
        temp = []
        for j in i:
            if j == '_':
                temp.append('_')
            else:
                temp.append(str(j))
        file.write(';'.join(temp) + '\n')
    file.close
    return '/tmp/' + user_ID + '.plan'