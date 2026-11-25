# def coin_change(amount,coins):
#     coins.sort(reverse=True)
#     cnt=0
#     d1={}

#     for coin in coins:
#         while amount >=coin:
#             cnt+=1
#             amount -=coin
#             if coin not in d1:
#                 d1[coin]=1
#             else:
#                 d1[coin]=1

#     print('Tottal coins: ', cnt)
#     for k,v in d1.items():
#         print(k,'*', v,'=',k*v)



# coins= [2,10,500,20,50,100,5,20,1000,500,2000,1,200]
# amount=6852
# coin_change(amount,coins)







#2nd Proggrammm

def activity_selection(activities):
    print(activities)
    activities.sort(key= lambda x: x[2])
    print(activities)


    i=0
    print(activities[i][0],end=' ')
    for j in range(len(activities)):
        if activities[j][1]>activities[i][2]:
            print(activities[j][0],end=' ')
            i=j

activities=[
      ['A1',0,6]
      ['A2',3,4]
      ['A3',1,2]
      ['A4',5,8]
      ['A5',5,7]
      ['A6',8,9]

]




#assinment

'''  In a problemstatmet given a arrival and departure timings of a train as follows
    arrival= [900,940,950,1100,1500,1800]
    departure=[910,1200,1120,1130,1900,2000]




    2- Find the total no. of Platforms required to handle all this trains without providing waiting time
    for another train

'''