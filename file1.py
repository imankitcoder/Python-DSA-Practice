class STACK:
    def __init__(self):
        self.s1=[]
    def display(self):
        if self.s1 !=0:
            for i in range (len(self.s1)-1,-1,-1):
                print(self.s1[i])
        else:
            print('0 Elements to fetch')

    def push(self,val):
        self.s1+=val
    def pop(self):
        self.s1.pop()

    def peek(self):
        print(f'The top element of the stack is {self.s1[-1]}')
st= STACK()
st.push('A')
st.push('b')
st.push('C')
st.push('D')
st.push('E')
st.push('F')
st.display()