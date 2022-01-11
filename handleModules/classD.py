from module_A.classA import A
from module_B.classB import B
from module_C.classC import C


class D(object):
    def __init__(self):
        super().__init__()

    def print_data(self):
        print("data of class D")

    def print_data_in_classes(self):
        a = A()
        b = B()
        c = C()
        a.print_data()
        b.print_data()
        c.print_data_in_classes()


if __name__ == '__main__':
    d = D()
    d.print_data_in_classes()
