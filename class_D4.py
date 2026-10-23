#23OCt 2026
def Is_Balanced(s1):
    stack= []
    d1= {
        '}': '{',
        ')': '(',
        ']': '['
}

    for i in s1:
        if i in "({[":
            stack.append(i)
        else:
            if not stack or d1[i] != stack.pop():
                return False
    return len(stack)==0

# s1= '((({})))'
s1= '((({}))]])'
if Is_Balanced(s1):
    print("Balanced")
else:
    print(" Not Balanced ")

#______________________________________________________________________________________
#wap to evaluate postfix expression

def Postfix_expression(s1):
    stack= []
    for i in s1:
        if ord(i)>= 49 and ord(i) <=57:
            stack.append(int(i))
        else:
            n1= stack.pop()
            n2= stack.pop()

            if i == '+':
                stack.append(n1+n2)
            elif i =='-':

                stack.append(n1-n2)
            elif i == '*':

                stack.append(n1*n2)
            elif i== '/':

                stack.append(n1/n2)
            elif i=='%':
                stack.append(n1+n2)

    return stack.pop()
s1= "23"  
print(s1)
print(Postfix_expression(s1)) 


#wap to insert a queue data structure in stack data structure

