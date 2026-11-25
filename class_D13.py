def partition(start,end,l1):
    print(l1)
    i = start
    k= end-1
    pivot= l1[end]


    while i< j:
        while l1[i] <pivot:
            i+=1

        while l1[j]>pivot:
         j-=1

         if i< j :
            l1[i] , l1[j]= l1[j],l1[i]

    # print(l1)
    
    return i

l1=[3,5,8,1,2,9,4,7,6
    ]
print(l1)
