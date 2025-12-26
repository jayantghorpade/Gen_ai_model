sum=0
def add(val):
    global sum
    if val>0:
        sum=sum+val
        add(val-1)
    return sum
        


add(2)