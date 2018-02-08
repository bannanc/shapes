"""
Testing area package
"""

from shapes.square.area import area_square
from shapes.square.perimeter import perimeter_square
from shapes.triangle.area import area_triangle
import pytest


def test_square_area():
    """
    testing function area_square
    """
    length = 2
    A = area_square(length)
    assert pytest.approx(A) == 4.0


def test_square_perimeter():
    """
    testing function perimeter_square
    """
    length = 2
    P = perimeter_square(length)
    assert pytest.approx(P) == 8.0


def test_triangle_area():
    """
    testing function area_triangle
    """
    base = 4
    height = 5
    A = area_triangle(base, height)
    assert pytest.approx(A) == 10.0


