class Stack(object):


    def __init__(self):
        """Initialize an empty stack."""
        self.ll = []
        self.top = 0

    def push(self, item):
      self.ll.insert(self.top,item)
      self.top+=1
      print ("push" + ": " +str( item))
      print ("top=" + str(self.top))

    def pop(self):
        self.top -= 1
        print ("pop : "+ str(self.ll.pop(self.top)))



if __name__ == "__main__":
    print("Stack using list.")
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)
    s.pop()
    s.pop()
    s.pop()
