def dp(a,b):
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]*b[i]
    return sum
def transpose(a):
    return [list(i) for i in zip(*a)]
def matmult(a,b):
    result=[]
    try:
        b=transpose(b)
        for aa in a:
            initial=[]
            for bb in b:
                initial.append(dp(aa,bb))
            result.append(initial)
        return result
    except:        
        # if it gets here then implies that b is a 1d array
        try:
            for i in a:
                result.append(dp(i,b)) # for each a[i], find the dot product with b
            return result
        except:
            return dp(a,b)
def magic(number):
    try:
        return float(''.join(str(i) for i in number))
    # example -> x=[2,3] -> '23' -> 23
    except:
            return int(''.join(str(i) for i in number))
def result(a,b):
    # b must be an element in a
    a=sorted(a)
    if abs(b - (a[a.index(b)-1])) < abs(b - (a[a.index(b)+1])):
        return a.index(b)-1
    return a.index(b)+1
# All function in this file have been certified!
