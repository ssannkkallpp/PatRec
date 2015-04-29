from PIL import Image
from numpy import *
from itertools import *
import itertools
import numpy as np
def init(x):
    img = Image.open(x)
    img.size=(150,150)
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
    arr, arr_transpose=np.matrix(arr), np.matrix(arr_transpose)
    x=array([1,0,0,0])
    val=arr * arr_transpose
    val=array(val)
    return val * x
print main("/Users/sankalpyohanramesh/Google Drive/numset/testset/I1.png")
