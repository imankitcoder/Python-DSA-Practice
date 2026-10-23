# Stack implementation without giving size
class STACK:
    def __init__(self):
        self.s1=[]

    def display(self):
        if len(self.s1)!=0:
            for i in range (len(self.s1)-1,-1,-1):
                print(self.s1[i])
        else:
            print('Stack has 0 elements ')
    def push(self,val):
        self.s1+= val

    def pop(self):
        self.s1.pop()

    def peek(self):
        print('Top of the element of the stack is : ', self.s1[-1])
st= STACK()
st.push('a')
st.push('1')
st.display()

_______________________________________________________________________________________________

# Example 2: Stack implementation with limit size

class STACK:
    def __init__(self,maxsize):
        self.maxsize= maxsize
        self.s1=[]

    def IsFull(self):
        if len(self.s1)== self.maxsize:
            return True
        else:
            return False

    def push(self,val):
        if self.IsFull():
            print("Stack is Full ")
        else:
            self.s1.append(val)

    def IsEmpty(self):
        if len(self.s1)==0:
            return True
        else:
            return False

    def peek_ele(self):
        if self.IsEmpty():
            print("No elements")
        else:
            print ("Top elements of the stack is " ,self.s1[-1])

    def pop(self):
        if self.IsEmpty():
            print("no elements to remove")
        else:
            self.s1.pop()
    def display(self):
        if len(self.s1)!=0:
            for i in range (len(self.s1)-1,-1,-1):
                print(self.s1[i])
        else:
            print("stack has 0 elemts")


st= STACK(5)
while True:
    print('===============Stack Operations====================')
    print("1.IsFull\n 2.IsEmpty\n 3.Push \n 4.pop\n 5.peek\n 6.Display\n7.exit")

    opt= int(input('Enter the option you want to perform: '))
    match opt:
        case 1 :
          print('Is stack is full',st.IsFull())
        case 2:
            print("Is stack is empy ",st.IsEmpty())
        case 3:
            print("Push the elemet ")
            val= int(input('"enter the element: '))
            st.push(val)
        case 4:
            st.pop()
        case 5:
            st.peek_ele
        case 6:
            st.display()
        case 7:
            print("exiting")
            break

        case _:
            print("invalid option ")
____________________________
-----------------------------------------------------------------------------------------------
# Using Recursion to implement stack sum of natural no. 

def sumofnum(n):
    if n==1:
        return 1
    else:
        return n + sumofnum(n-1)
print(sumofnum(10))




_______________________________________________________________________________________
# Program to find sum of a given without using the loop

def sumnum(n):
    if n==0:
        return False
    else:
        return n%10 + sumnum(n//10)


print(sumnum(321))

________________________________________________________________________________________
# sum of given list using Reccursion
def sumoflist(l1):
    if (len(l1))== 0:
        return 0 
    else:
        return l1[0]+ sumoflist(l1[1:])
print(sumoflist([1,2,3,45,6,6,7,7,8]))

___________________________________________________________________________________________



