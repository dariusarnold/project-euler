import numpy as np

def is_palindrome(num):
    """
    :param num:
    :type num: int
    :return:
    :rtype:
    """
    num_str = str(num)
    while len(num_str) > 0:
        if num_str[0] == num_str[-1]:
            num_str = num_str[1:-1]
        else:
            return False
    return True


a = np.arange(999, 99, step=-1)
b = a.copy()

multiplications = np.outer(a, b)
multiplications = multiplications.flatten()
multiplications = np.sort(multiplications)[::-1]

for entry in multiplications:
    if (is_palindrome(entry)) is True:
        print(entry)
        exit()