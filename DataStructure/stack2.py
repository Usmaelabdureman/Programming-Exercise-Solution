class Stack2():
    def __init__(self):
        self.__stack2 = []
        # self.maxsize=8
    def push(self,data):
        self.__stack2.append(data)
        # print("list doesn't have enough space")
    def pop(self):
        return self.__stack2.pop()
    def peek(self):
        return self.__stack2[len(self.__stack2)-1]
    def is_empty(self):
        return len(self.__stack2)==0
    def GetSize2(self):
        return len(self.__stack2)

    # def isFull(self):True if (len(self.Stack)==maxsize) else False

    # def PrintStack(self):
    #     if self.is_empty():
    #         raise IndexError('Stack is empty')
    #     cur=0
    #     while(cur<len(self.__stack2)):
    #         print(str(self.__stack2[cur])+'',end=' ')
    #         cur+=1
    #     print()
