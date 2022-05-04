
class Stack():
    def __init__(self):
        self.__stack1 = []
        # self.maxsize=8
    def push(self,data):
        self.__stack1.append(data)
        # print("list doesn't have enough space")
    def pop(self):
        return self.__stack1.pop()
    def peek(self):
        return self.__stack1[len(self.__stack1)-1]
    def is_empty(self):
        return len(self.__stack1)==0
    def GetSize1(self):

        return len(self.__stack1)

    # def isFull(self):True if (len(self.Stack)==maxsize) else False

    # def PrintStack(self):
    #     if self.is_empty():
    #         raise IndexError('Stack is empty')
    #     cur=0
    #     while(cur<len(self.__stack1)):
    #         print(str(self.__stack1[cur])+'',end=' ')
    #         cur+=1
    #     print()
def __test__():
    a = Stack()
    a.push('test')
    a.push(23)
    a.push(True)
    a.push(45)
    a.push("usmael")
    a.push(8)
    a.push(8)
    a.push(87)
    a.push(67)
    a.push(34)
    a.push(90)
    # a.PrintStack()
    a.peek()
    print( "after peek")
   
    print(a.pop())
    print("After pop ")
    while(a.GetSize1()>0):
        print(a.pop())
    print()
    
    
if __name__ == '__main__':
    __test__()