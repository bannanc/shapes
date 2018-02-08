"""
This script contains functions to calculate the area of a triangle
"""


def area_triangle(base, height):
    """
    .. math::

        area =  \\frac{base * height}{2.0}

    Parameters
    ----------
    base: float
        length of the base of the triangle
    height: float
        height of the triangle

    Returns
    -------
    area: float
        area of the triangle
    """
    return (base * height) / 2.0
