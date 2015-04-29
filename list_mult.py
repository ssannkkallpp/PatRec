def list_mult(a,b):
    # lists a and b have to be equal
    total=0
    if len(a) == len(b):
        for i in range(0,len(a)):
            total+=a[i]*b[i]
        return total
    return  
