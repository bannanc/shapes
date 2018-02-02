"""
Testing area package
"""

from shapes.square.area import area_square
from shapes.square.perimeter import perimeter_square
import pytest


def test_square_area():
    """
    testing function area_square
    """
    length = 2
    A = area_square(length)
    assert pytest.approx(A) == 4.0


def test_square_perimeter():
    length = 2
    P = perimeter_square(length)
    assert pytest.approx(P) == 8.0


######################
# Write a test for the triangle function
######################
def test_triangle_area():
    print("insert test for triangle area here")

