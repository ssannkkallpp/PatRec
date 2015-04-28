from PIL import Image
from numpy import *
from itertools import *
import itertools
from sys import *
import sys

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
    arr=array(arr)
    in_ar=init(input_file)
    loc_globe=arr * arr.transpose()
    for i in range(0,51):
        x=loc_globe * x
        total=0
        for j in itertools.chain(*x):
            total+=j**2
        x=x/total
    y=a.transpose() * x
    final_arr=[y*m for m in arr]
    final_in = y * in_arr
    return final_arr, final_in                                                                                                                
print main(sys.argv[-1])
