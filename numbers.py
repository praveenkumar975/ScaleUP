for i in range(2,500):
    for j in range(2,500):
        if i%j==0:
           break
    if i==j:
        print(j,end=' ')