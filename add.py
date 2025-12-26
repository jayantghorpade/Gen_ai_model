sum=0
def add(val):
    global sum
    if val>0:
        sum=sum+val
        add(val-1)
<<<<<<< HEAD
    return sum,34
=======
    else:
        print(sum)
>>>>>>> design
        


add(2)