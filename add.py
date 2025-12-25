sum=0
def add(val):
    global sum
    if val>0:
        sum=sum+val
        add(val-1)
    else:
        print(sum)
        


add(2)