#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Admin
#
# Created:     26-08-2016
# Copyright:   (c) Admin 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0,item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)



def main():
        s = Stack()
        s.push('hello')
        s.push('true')
        print(s.pop())
        m = Stack()
        m.push('x')
        m.push('y')
        m.push('z')
        print(m)



if __name__ == '__main__':
    main()
