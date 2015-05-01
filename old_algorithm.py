from PIL import Image
from numpy import *
from itertools import *
from itertools import product
import itertools
import numpy as np
def multiply( mtx_a, mtx_b):
    tpos_b = zip( *mtx_b)
    rtn = [[ sum( ea*eb for ea,eb in zip(a,b)) for b in tpos_b] for a in mtx_a]
    return rtn
def divide(a,b):
    a=np.array(a)
    np.seterr(divide='ignore', invalid='ignore')
    b=b+0.0
    y=a/b
    return y.tolist()
def init(x):
    img = Image.open(x)
    img.size=(75,75)
    arr = array(img)
    new_arr=list(itertools.chain(*arr)) # flattens arr into a 1d array
    # example -> [[3,4],[2,3]] -> [3,4,2,3]
    av_arr=[list(i) for i in new_arr]
    av_arr=[sum(x)/len(x) for x in av_arr]
    return av_arr
def main(input_file):
    arr=[init(str(i)+'.png') for i in range(1,6)]
    # arr is the 2d matrix with each row representing one of the 5 images.
    in_arr=init(input_file)
    arr_transpose=[list(i) for i in zip(*arr)]
    val=multiply(arr,arr_transpose)
    x=[[1,0],[0,0]]
    for i in range(0,51):
        x=multiply(val,x)
        total=0
        for m in list(itertools.chain(*x)):
            total+=m
        x=divide(x,total)
    y=multiply(arr_transpose,x)
    final_arr=[multiply(y,arr[i]) for i in range(0,len(arr))]
print main("/Users/sankalpyohanramesh/Google Drive/numset/testset/I1.png")
