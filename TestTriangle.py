# -*- coding: utf-8 -*-
"""
Updated Sept 18, 2021
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Viyeta Kansara

"""

import unittest

from triangle import classify_triangle

# This code implements the unit test functionality


class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self):
        """Testing for right triangle."""
        self.assertEqual(
            classify_triangle(3, 4, 5), "Right", "3,4,5 is a Right triangle"
        )
        # self.assertEqual(classifyTriangle(6, 8, 10), 'Right', '6, 8, 10 is a Right triangle')

    def testRightTriangleB(self):
        """Testing for right triangle."""
        self.assertEqual(
            classify_triangle(5, 3, 4), "Right", "5,3,4 is a Right triangle"
        )

    def testEquilateralTriangles(self):
        """Testing for Equilateral triangle."""
        self.assertEqual(
            classify_triangle(1, 1, 1), "Equilateral", "1,1,1 should be equilateral"
        )
        self.assertEqual(
            classify_triangle(10, 10, 10),
            "Equilateral",
            "10, 10, 10 is a Equilateral triangle",
        )
        self.assertNotEqual(
            classify_triangle(19, 9, 9),
            "Equilateral",
            "9, 9, 13 is not a Equilateral triangle",
        )

    def testIsoscelesTriangles(self):
        """Testing for Isosceles triangle."""
        self.assertEqual(
            classify_triangle(9, 9, 13), "Isosceles", "9, 9, 13 is a Isosceles triangle"
        )
        self.assertEqual(
            classify_triangle(8, 12, 8), "Isosceles", "8, 12, 8 is a Isosceles triangle"
        )

    def testScaleneTriangles(self):
        """Testing for Scalene triangle."""
        self.assertEqual(
            classify_triangle(11, 12, 13), "Scalene", "11, 12, 13 is a Scalene triangle"
        )
        self.assertEqual(
            classify_triangle(10, 20, 15), "Scalene", "10, 20, 15 is a Scalene triangle"
        )

    def testNotATriangle(self):
        """Testing for Not a triangle."""
        self.assertEqual(
            classify_triangle(1, 1, 10), "NotATriangle", "1, 1, 10 is not a triangle"
        )
        self.assertEqual(
            classify_triangle(1, 10, 12), "NotATriangle", "1, 10, 12 is not a triangle"
        )

    def testInvalidInput(self):
        """Testing for Invalid Inputs."""
        self.assertEqual(
            classify_triangle(220, 0, 20),
            "InvalidInput",
            "220, 0, 20 is not a valid input",
        )
        self.assertEqual(
            classify_triangle(-5, 10, 20),
            "InvalidInput",
            "-5, 10, 20 is not a valid input",
        )
        self.assertEqual(
            classify_triangle(0, 5, 10), "InvalidInput", "0, 5, 10 is not a valid input"
        )
        self.assertEqual(
            classify_triangle("0", 5, 10),
            "InvalidInput",
            "'0', 5, 10 is not a valid input",
        )
        self.assertEqual(
            classify_triangle([5], 5, 10),
            "InvalidInput",
            "[5], 5, 10 is not a valid input",
        )


if __name__ == "__main__":
    print("Running unit tests")
    unittest.main()
