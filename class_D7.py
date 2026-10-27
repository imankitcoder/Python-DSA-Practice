class Node:
    def __init__(self,data):
        self.data= data
        self.addr= None


class Single_linked_List:
    def __init__(self):
        self.head= None

    def insertion_at_last(self,val):
        newNode= Node(val)
        if self.head is None:
            self.head= newNode
        else:
            temp= self.head
            while temp.addr != None:
                temp= temp.addr
            temp.addr= newNode
    def display(self):
        if self.head is None:
            print('No Nodes in single linked list')
        else:
            temp= self.head
            while temp:
                print(temp.data,end= " ->")
                temp = temp.addr
            print()

    def length(self):
            if self.head is None:
                print('No Nodes in single linked list')
            else:
                temp= self.head
                cnt=0
                while temp:
                    cnt+=1
                    temp= temp.addr
                return cnt
            print(cnt)

sll= Single_linked_List()
sll.insertion_at_last(10)
sll.insertion_at_last(20)
sll.insertion_at_last(30)
sll.insertion_at_last(30)
sll.insertion_at_last(30)
sll.display()
sll.length()