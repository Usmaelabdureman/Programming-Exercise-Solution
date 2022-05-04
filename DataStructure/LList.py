
class Node:
    def __init__(self,__data):
        self.__data=__data
        self.__next=None

class LinkedListIterator:
    def __init__ (self,__head):
        self.current=__head
    def __next__(self):
        if self.current==None:
            raise StopIteration
        __data=self.current.__data
        self.current=self.current.__next
        return __data
    
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None

    def __iter__(self):
        return LinkedListIterator(self.__head)
        
    def isEmpty(self):

        return self.__head.__next is None

    def Printer(self):
        if self.isEmpty is True:
            print("Linked list is Empty. Add few elements...")
        current=self.__head
        while current!=None:
            print(current.__data)
            current=current.__next
    def AddFirst(self,__data):
        node=Node(__data)
        node.__next=self.__head
        self.__head=node
        
    def AddLast(self,__data):
        newNode=Node(__data)
        last=self.__head

        while last.__next is not None:
            last=last.__next
        last.__next=newNode
    def GetSize(self):
        cur=self.__head
        count=0
        while (cur):
            cur=cur.__next
            count+=1
        return count
        
    def Insert(self,index,__data):
        current=self.__head
        j=1
        while (j<index):
            current=current.__next
            j+=1
        nod=Node(__data)
        nod.__next=current.__next
        current.__next=nod
    def GetFirst(self):
        if self.isEmpty():
            return print("Can't get from empty list")
        return self.__head.__data
    def GetLast(self):
        if self.isEmpty():
            return print("Can't get from empty list")
        else:
            cur=self.__head
            while(cur.__next!=None):
                cur=cur.__next
            if cur.__next==None:
                return cur.__data
    def RemoveFirst(self):
        first=self.__head
        self.__head=self.__head.__next
        first=None
        return self.__head.__next
    def Reverse(self):
        cur=self.__head
        while (cur):
            __next=cur.__next
            cur.__next=self.__tail
            self.__tail=cur
            cur=__next
        self.__head=self.__tail
    def Clear(self):
        self.__head=self.__tail=None

    def Contains(self,element):
        current=self.__head
        while current!=None:
            if current.__data==element:
                return True
            current=current.__next
        return False
            

def test():
    lists=LinkedList()
    lists.AddFirst(5)
    lists.AddLast(4)
    lists.AddFirst(8)
    # lists.AddLast(7)
    lists.AddFirst(10)
    lists.AddFirst(49)
    lists.AddFirst(33)
    lists.AddLast(11)
    lists.Insert(2,14)
    lists.AddFirst(20)
   
    
    lists.Printer()
    print(" Size is =",lists.GetSize())
    print(lists.GetFirst())
    print(lists.GetLast())
    lists.RemoveFirst()
    print("*"*10)
    print(lists.GetFirst())
    print("*"*10)
    lists.Reverse()
    lists.Printer()
    print("element 10 is in list ",lists.Contains(10))
    print("element 19 is in list ",lists.Contains(19))
    
test()
                
        