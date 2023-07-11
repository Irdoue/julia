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
    """
    Return the n_th iteration of the c-julia progression for the complex z.

    :param n: the last step of the progression
    :type n: int
    :parap z: The initial complex term of the progression
    :type z: complex
    :param c: The associated constant of the Julia's progression
    :type c: complex
    :return: The n_th term of the c-julia progression for the complex z if it modulus is less than two, None else.
    :rtype: float or None

    """
    for i in range(n):
        if modulus(z) >= 2:
            return 1
        z = z**2 + c
        z = approx(z, d)
    return z

def modulus(z):
    """
    Return the modulus of a complex.

    :param z: A complex.
    :type z: complex
    :return: The modulus of z.
    :rtype: float

    """
# n the rank
# c the constant
def make_julia(n, c):
    """
    Return the c-julia trail of n iteration.

    :param n: The number of iteration.
    :type n: int
    :param c: The associated constant of the Julia's set.
    :type c: complex
    :return: A matrice of complex representing the Julia's set.
    :rtype: list[list[complex]]

    """
    julia = []
    temp = []
    for l in np.linspace(-2, 2, 4 * 10**2 + 1):
        for k in np.linspace(-2, 2, 4 * 10**2 + 1):
            temp.append(modulus(make_progression(n, complex(k, l), c)))
        julia.insert(0, temp)
        temp = []
    return julia

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
    return z

    """
    Return the plan of complex.

    :param decimal: The number of decimal in each complex.
    :type decimal: int
    :return: The plan of complex with the selected number of decimal.
    :rtype: list[list[complex]]

    """
    plan = []
    temp = []
    for l in np.linspace(-2, 2, 4 * 10**n + 1):
        for k in np.linspace(-2, 2, 4 * 10**n + 1):
            temp.append(approx(complex(k, l), d))
        plan.insert(0, temp)
        temp = []
    return plan

    """
    Return the next step of an actual c-julia step.

    :param julia: The actual Julia's trail.
    :type julia: list[list[complex]]
    :param c: The associated Julia's constant.
    :type c: complex
    :return: A matrice of complex representing the Julia's set.
    :rtype: list[list[complex]]

    """
    for l in range(len(temp)):
        for k in range(len(temp)):
            temp[l][k] = make_step(temp[l][k], c)
    return temp

    """
    Make and save the Julia's set with a specified name in ./pictures/ .

    :param julia: A Julia's trail.
    :type julia: list[list[complex]]
    :param name: The name of the saved picture.
    :type name: str

    """
    for l in range(len(temp)):
        for k in range(len(temp)):
    """
    Make two collection of pictures.
    The first one are the successiv step of a c-julia.
    The second one are some of the Julia's trail of complex with same modulus but different argument.

    :param decimal: The number of decimal in each complex.
    :type decimal: int
    :param step_number: The number of iteration.
    :type step_number: int
    :param t: The number of Julia's trail of the second part.
    :type t: int
    :param constant: Optional associated constant of the Julia's. If unspecified, will be a random complex.
    :type constant: complex

    """
