for x in range(3,21):
    rezult = ''
    for  i in range(1,x):
        for j in range(i+1,20):
            if x % (i+j) == 0:
                rezult += str(i)
                rezult += str(j)
            else:
                    continue
    print (x ,'-',rezult)
