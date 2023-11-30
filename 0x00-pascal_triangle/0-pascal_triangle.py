#!/usr/bin/python3
"""Determines pascal's triangle for any number"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal’s triangle of n
    """
    triangle = []

    if n <= 0:
        return triangle
    for j in range(n):
        temp_list = []

        for i in range(j+1):
            if i == 0 or i == j:
                temp_list.append(1)
            else:
                temp_list.append(triangle[j-1][i-1] + triangle[j-1][i])
        triangle.append(temp_list)
    return triangle
