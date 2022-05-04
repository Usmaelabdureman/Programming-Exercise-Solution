
from Stack import Stack
from stack2 import Stack2

class Queue:
    def __init__(self):
        self.element1=Stack()
        self.element2=Stack2()

    def Enqueue(self,data):
        self.element1.push(data)

    def Dequeue(self):
        while (self.element1.GetSize1()>0):
            self.element2.push(self.element1.pop())
        return self.element2.pop()


    # def GetElement1(self,data):
    #     data=self.element1.pop()
    #     return 



    def GetSize1(self):
        return self.element1.GetSize1()
    # def GetSize2(self):
    #     return self.element2.GetSize2()



def main():
    myq=Queue()
    myq.Enqueue(9)
    myq.Enqueue(40)
    myq.Enqueue(60)
    myq.Enqueue(80)

    while(myq.GetSize1()>0):
        print(myq.Dequeue())
    print()
main()





















#     def enQueue(self, x)
#         while len(self.s1) != 0:
#             self.s2.append(self.s1[-1])
#             self.s1.pop()

#     # Push item into self.s1
#     self.s1.append(x)

#     # Push everything back to s1
#     while len(self.s2) != 0:
#         self.s1.append(self.s2[-1])
#         self.s2.pop()

# # Dequeue an item from the queue
# def deQueue(self):
        
#         # if first stack is empty
#     if len(self.s1) == 0:
#         print("Q is Empty")
    
#     # Return top of self.s1
#     x = self.s1[-1]
#     self.s1.pop()
#     return x
