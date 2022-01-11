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
