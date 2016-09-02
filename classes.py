#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     29-06-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class cricket:
    def __init__(self):
        print("this is not constructor")
        self.car="a"
        print(self.car)
        self.typ="petdie"
        print(self.typ)
    def lam(self):
        self.car="lamborghini"
        print(self.car)
        self.typ="petrol"
        print(self.typ)
    def fer(self):
        car="ferrari"
        print(car)
        typ="diesel"
        print(typ)


def main():
        obj=cricket()
        obj.lam()
        obj.fer()

if __name__ == '__main__':
    main()
