'''
String Challenge

Have the function to insert dashes between each two odd numbers, For example if at is 454793 the output should be 4547-9-3. Don't count zero as an odd number
Once your function is working, take the final output string and concatenate it with your ChallengeToken, and then replace every third character with an X.

Your ChallengeToken: Ifvuixty14b

Examples

Input: 99946
Output: 9-9-946
Final Output: 9-X-9x61XvuXxX14X
'''

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
    for i in "Ifvuixty14b":
        tmp.append(i)
    print(tmp)
    for i in range(1,len(tmp)):
        if i%3==0:
            tmp[i-1]='X'
    new = ''.join(tmp)
    print(new)
fun("233475645556")  
