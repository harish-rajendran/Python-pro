#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     21-07-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class player:
    personage=10
    name="RAM"
    tape="sub"

    def __init__(self,p,age):
        print("hi")
        self.personage=age
        self.tape=p
class play(player):

    def check(self):
        print(self.personage)
        print(self.name)
        print(self.tape)

def main():
    sach=play("god",78)
    sach.check()
    wall=play("batsman",65)
    wall.check()


if __name__ == '__main__':
    main()
