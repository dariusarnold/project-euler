#!/usr/bin/env python

"""
Solution for exercise 18 and 67, which are both maximum path sums through a triangle.
18 is small and can be solved by a recursive function.
https://projecteuler.net/problem=18
Solving 67 requires a faster algorithm. Here a dynamic iterative approach is used.
https://projecteuler.net/problem=67
"""

def max_triangle_sum_recursive(triangle, row, col):
    """
    Calculate the max sum for a path in a triangle from top to bottom.
    Works by going top down always looking at a smaller triangle until in the last row, where the value is returned.
    In the row above the maximum of the two returned values is added to the current value, which is the returned.
    :param triangle: Triangle as a list of lists of integers. The triangle can be accessed by triangle[row][column]
    :type triangle: [[int]]
    :return: Max sum for a path through the triangle
    :rtype: int
    """
    if row == len(triangle)-1: return triangle[row][col]
    return triangle[row][col] + max(max_triangle_sum_recursive(triangle, row + 1, col), max_triangle_sum_recursive(triangle, row + 1, col + 1))


def max_triangle_sum_bottom_up(triangle):
    """
    Calculate the max sum for a path in a triangle from top to bottom.
    Works by going bottom up and adding to every entry in a line the max of the lower left and the lower right entry.
    :param triangle: Triangle as a list of lists of integers. The triangle can be accessed by triangle[row][column]
    :type triangle: [[int]]
    :return: Max sum for a path through the triangle
    :rtype: int
    """

    def _get_lower_left(triangle, row, col):
        return triangle[row + 1][col]

    def _get_lower_right(triangle, row, col):
        return triangle[row + 1][col + 1]

    # start adding from second to last row
    row_index = len(triangle) - 2
    while row_index >= 0:
        for col_index, ele in enumerate(triangle[row_index]):
            left = _get_lower_left(triangle, row_index, col_index)
            right = _get_lower_right(triangle, row_index, col_index)
            triangle[row_index][col_index] = ele + max(left, right)
        row_index -= 1
    return triangle[0][0]

def convert_triangle_text_to_list(triangle):
    # split into lines
    triangle = triangle.splitlines(keepends=False)
    # split every line in strings
    triangle = [line.split(' ') for line in triangle]
    # convert line containing strings to list of ints
    triangle = [[int(entry) for entry in line if entry != ''] for line in triangle]
    return triangle


def read_triangle_file(filename):
    with open(filename) as f:
        triangle = f.readlines()
    # remove newline from end of line
    triangle = [line.split() for line in triangle if line != '']
    # convert to list of integers
    triangle = [[int(entry) for entry in line] for line in triangle]
    return triangle


def solve_small_triangle():
    triangle = """\
    75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    triangle = convert_triangle_text_to_list(triangle)
    print(max_triangle_sum_recursive(triangle, 0, 0))

def solve_big_triangle():
    triangle = read_triangle_file("/home/darius/triangle.txt")
    print(max_triangle_sum_bottom_up(triangle))

if __name__ == '__main__':
    solve_big_triangle()