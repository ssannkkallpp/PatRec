from PIL import Image
from numpy import *
from itertools import *
import itertools
def compare(a,b):
    x=[max(a[i],b[i])-min(a[i],b[i]) ** 2 for i in range(0,len(a))]
    return sum(x), b
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
    arr=[init(str(i)+'.png') for i in range(0,10)]
    in_arr=init(input_file)
    minimum=compare(in_arr,arr[0])
    for x in arr:
        if compare(in_arr, x)[0] < minimum[0]:
            minimum=compare(in_arr,x)
    return arr.index(minimum[-1])
print main("/Users/sankalpyohanramesh/Google Drive/numset/testset/Impact1.png")
