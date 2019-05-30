from collections import Counter

sent=str(input('Write a string with special characters: '))
newsent = (split(sent))
n=len(newsent)
speclist=[]
i=0

while i < n:
    if (ord(newsent[i])< 65 and ord(newsent[i])>90) and (ord(newsent[i])<97 and ord(newsent[i])>122):
        x=newsent[i]
        speclist.append(x)
        i = i+1

Counter(speclist)
