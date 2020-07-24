class deque:
#functions to add, remove and initiate
    
    def __init__(self):
        self.arr = [2, 2, 3, 4, 5, 6, 3, 4, 2, 3, 4]
        self.max = 20

    def addToFront(self, x):
        if len(self.arr) == self.max:
            return "The deck is full"
        else:
            self.arr.insert(0,x)
        
    def addToBack(self, x):
        if len(self.arr) == self.max:
            return "The deck is full"
        else:
            self.arr.append(x)

    def removeFront(self):
        if self.arr != []:
            self.arr.pop()
        else:
            return "The deque is empty"
        
    def removeBack(self):
        if self.arr != []:
            self.arr.pop(0)
        else:
            return "The deque is empty"
        
    def size(self):
        if self.arr == []:
            return None
        elif len(self.arr) == self.max:
            return "The deck is full"
        else:
            return len(self.arr)
    
    def isEmpty(self):
        if(self.arr) == []:
            return True
        else:
            return False
    
    def getFront(self):
        return self.arr[-1]
    
    def getBack(self):
        return self.arr[0]
    
    def __repr__(self):
        "Object : {}".format(self.arr)
        
if __name__ == "__main__":
    deq = deque()
    deq.addToFront(0.1)
    deq.addToBack(1)
    print("The front is", deq.getFront())
    print("Index: ", deq.size())