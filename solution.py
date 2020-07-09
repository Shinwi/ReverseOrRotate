#reverse or rotate

def revrot(s, sz):
    ans = []
    if sz<=0 or len(s)==0 or sz>len(s):
        return ""
    else:
        chunks = [ s[i:i+sz] for i in range(0, len(s), sz)]
        #removing the last part of the list if it is smaller than sz
        if len(chunks[-1])<sz:
            chunks.remove(chunks[-1])
        #checking if the sum of the cubes of its digits is divisible by 2
        for i in range(len(chunks)):
            value = 0
            for j in chunks[i]:
                value += int(j)*int(j)*int(j)
            if value%2 == 0:
                reverse = chunks[i][::-1]
                ans.append(reverse)
            else:
                rotate = chunks[i][1:]+chunks[i][0]
                ans.append(rotate)
    return "".join(ans)


#testcases:
# revrot("123456987654", 6) --> "234561876549"
# revrot("123456987653", 6) --> "234561356789"
# revrot("66443875", 4) --> "44668753"
# revrot("66443875", 8) --> "64438756"
# revrot("664438769", 8) --> "67834466"
# revrot("123456779", 8) --> "23456771"
# revrot("", 8) --> ""
# revrot("123456779", 0) --> "" 
# revrot("563000655734469485", 4) --> "0365065073456944"
