import os
import sys

# source: https://www.geeksforgeeks.org/python-import-from-parent-directory/
# getting the name of the directory
# where the this file is present.
current = os.path.dirname(os.path.realpath(__file__))

# Getting the parent directory name
# where the current directory is present.
parent = os.path.dirname(current)

# adding the parent directory to
# the sys.path.
sys.path.append(parent)

from module_A.classA import A
from module_B.classB import B


class C(object):
    def __init__(self):
        super().__init__()

    def print_data(self):
        print("data of class C")

    def print_data_in_classes(self):
        a = A()
        b = B()
        a.print_data()
        b.print_data()


if __name__ == '__main__':
    c = C()
    c.print_data()
    c.print_data_in_classes()
