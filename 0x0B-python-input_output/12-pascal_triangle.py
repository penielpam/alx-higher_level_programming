#!/usr/bin/python3
"""a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents size n in Pascal's Triangle.

    Returns a list of lists of integers which representsthe triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
