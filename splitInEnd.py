def spl_ad_end(l):
    li=[]
    for i in range(2,len(l)):
        print('index :',i,'\n','elem:',l[i])
        li.append(l[i])
    li.append(l[0])
    li.append(l[1])
    return li

print(spl_ad_end([2,3,4,5]))