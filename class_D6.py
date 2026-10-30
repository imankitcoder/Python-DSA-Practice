class STACK:
    def __init__(self,maxsize):
        self.maxsize= maxsize
        self.s1= []

    def push(self,val):
        if len(self.s1)>0 and len(self.s1[-1])<self.maxsize:
            self.s1[-1].append(val)
        else:
            self.s1.append([val])

    def display(self):
        print(self.s1)

    def display_stack(self,stackNum):
        if len(self.s1) !=0:
            if stackNum <= len(self.s1):
                print(self.s1[stackNum-1])   
            else:
                print('Given Stack Is not Presesent')
        else:
            print('Stack is Empty')

    def peek(self):
        if len(self.s1)==0:
            print('Stack is Empty')
        else:
            print(self.s1[-1][-1])

    def peekAt(self,stackNum):
        if len(self.s1) !=0:
            if stackNum <= len(self.s1):
                print(self.s1[stackNum-1][-1])
            else:
                print("Given Stack Num is not Present")
        else:
            print("Stack is Empty")

    def pop(self):
        if len(self.s1)==0:
            print('Stack is Empty')
        elif len(self.s1) and len (self.s1[-1])==0:
            self.s1.pop()   #here you should check vo jo list hai complete hatana hai yadi hat jaaye to
        else:
            self.s1[-1].pop()

    def popAt(self,stackNum):
        if len(self.s1) != 0:
            if stackNum<= len(self.s1):
                self.s1[stackNum-1].pop()
            else:
                print('Give Stack Num is not present')
        else:
            print('stack is Empty')

    def pushAt(self,stackNum,val):
        if len(self.s1)!=0:
            if stackNum <= len(self.s1):
                if len(self.s1)==self.maxsize:
                    print('stack number is full')
                else:
                    self.s1[stackNum-1].append(val)
            else:
                print('stack is empty')#you should check here it should be change simple codee
    

st= STACK(4)
st.push(10)
st.push(20)
st.push(30)
st.push(40)
st.push(50)
st.push(60)
st.display()
st.peek()
st.peekAt(1)