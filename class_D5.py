# class STACK:
#     def __init__(self):
#         self.s1= []

#     def push(self,val):
#         self.s1.append(val)

#     def pop(self):
#         return self.s1.pop()

#     def display(self):
#         print(self.s1)


# class QUEUE:
#     def __init__(self):
#         self.instack=STACK()
#         self.outstack= STACK()

#     def enqueue(self,val):
#         self.instack.push(val)

#     def dequeue(self):
#         while len(self.instack.s1):
#             self.outstack.push(self.instack.pop())
#         self.outstack.pop()
#         while len(self.outstack.s1):
#             self.instack.push(self.outstack.pop())

#     def q_display(self):
#         self.instack.display()

# q= QUEUE()
# q.enqueue(10)
# q.enqueue(20)
# q.enqueue(30)
# q.enqueue(40)

