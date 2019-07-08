char_no=256
def distinct(str,no):
    count1=[0]*char_no
    for loop in range(no):
        count1[ord(str[loop])]+=1
    maxi=0
    
    for loop in range(char_no):
        if(count1[loop]!=0):
            maxi+=1
    return maxi

def small_substr(str):
    n=len(str)
    max_dist=distinct(str,n)
    mini=n
    for i in range(n):
        for j in range(n):
            sub_str=str[i:j]
            sub_str_length=len(sub_str)
            sub_dist_char=distinct(sub_str,sub_str_length)
            if(sub_str_length<mini and max_dist == sub_dist_char):
                mini=sub_str_length
    return mini

inp=input()
op=small_substr(inp)
print(op)
