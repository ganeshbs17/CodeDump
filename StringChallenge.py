def fun(str):
    tmp=list(str)
    j=1
    #print(tmp)
    for i in range(0,len(tmp)-1):
        if int(str[i])%2 != 0 and int(str[i+1])%2!=0:
            #print(i)
            #print(str[i],str[i+1])
            tmp.insert(i+j,'-')
            j+=1
    #print(tmp)
    for i in "lxgiwyl":
        tmp.append(i)
    print(tmp)
    for i in range(1,len(tmp)):
        if i%3==0:
            tmp[i-1]='X'
    new = ''.join(tmp)
    print(new)
fun("233475645556")  
