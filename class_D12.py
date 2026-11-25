#BubbleSort>>

# def Bubble_sort(l1):
#     for i in range(len(l1)):
#         for j in range(i+1, len(l1)):
#             if l1[i] >l1[j]:
#                 l1[i],l1[j]= l1[j],l1[i]
# l1=[8,2,4,1,3]
# print('Before Bubble Sort', l1)
# Bubble_sort(l1)
# print('After Bubble Sort', l1)



#Single sort

# def selection_sort(l1):
#     for i in range(len(l1)):
#         min_ele= i
#         for j in range(i+1,len(l1)):
#             if l1[min_ele]>l1[j]:
#                 min_ele= j 
#         l1[i],l1[min_ele]= l1[min_ele],l1[i]

# l1=[2,-5,8,1,4,6,-6,1,0]
# print('Before',l1)
# selection_sort(l1)
# print('After',l1)


#Bucket Sort


import math
def Bucket_Sort(l1):
    #find the total buckets
    total_buckets= round(math.sqrt(len(l1)))
    print(total_buckets)

    #create Buckets

    buckets= []
    for _ in range(total_buckets):
        buckets.append([])
    print(buckets)

    #find the buckets number for each element


    for i in l1:
        bucket_num= math.ceil((i*total_buckets)/ max(l1))
        buckets[bucket_num-1].append(i)
    print(buckets)


    #sort each buckets
    for i in buckets:
        i.sort()
    print(buckets)

    #merge all the buckets
    k=0
    for i in range (total_buckets):
        for j in range(len(buckets[i])):
            l1[k]= buckets[i][j]
            k+=1

#hw merge the buckets
l1= [8,1,5,9,3,6,8,5,3,2,5]
print('bucketsort',l1)
Bucket_Sort(l1)
print(l1)