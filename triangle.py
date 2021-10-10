# -*- coding: utf-8 -*-
"""
Updated Sept 18, 2021

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Viyeta Kansara

"""


def classify_triangle(side_a, side_b, side_c) -> str:
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.

    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isosceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the square of the third side, then return 'Right'
    """

    # verify that all 3 inputs are integers
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not (
        isinstance(side_a, int) and isinstance(side_b, int) and isinstance(side_c, int)
    ):
        return "InvalidInput"

    # require that the input values be >= 0 and <= 200
    if side_a > 200 or side_b > 200 or side_c > 200:
        return "InvalidInput"

    if side_a <= 0 or side_b <= 0 or side_c <= 0:
        return "InvalidInput"

    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (
        (side_a >= (side_b + side_c))
        or (side_b >= (side_a + side_c))
        or (side_c >= (side_a + side_b))
    ):
        return "NotATriangle"

    # now we know that we have a valid triangle
    if side_a == side_b and side_b == side_c and side_c == side_a:
        return "Equilateral"
    elif (
        (side_a * side_a + side_b * side_b == side_c * side_c)
        or (side_c * side_c + side_b * side_b == side_a * side_a)
        or (side_a * side_a + side_c * side_c == side_b * side_b)
    ):
        return "Right"
    elif (side_a != side_b) and (side_b != side_c) and (side_a != side_c):
        return "Scalene"
    else:
        return "Isosceles"
