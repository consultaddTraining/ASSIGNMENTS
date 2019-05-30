
even_sum=[]
def even:
    for i in range(1,22):
        for j in range(i+1,22):
            if((i+j)%2==0) and (i+j) in range(1,21):
                even_sum.append(tuple((i,j)))

even()
print(even_sum)
