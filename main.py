import modules
import init
import matmult
def main(input_file):
    #---------------------------------------------#
    arr=[init.init(str(i) + '.png') for i in range(1,6)]
    arr_transpose=matmult.transpose(arr)
    val=matmult.matmult(arr, arr_transpose)
    #---------------------------------------------#
    in_arr=init.init(input_file)
    in_arr=[float(i) for i in in_arr]
    x=[0 for i in range(len(arr)-1)]
    x.append(1)
    #---------------------------------------------#
    for i in range(0,3):
        x=matmult.matmult(val, x)
        x=[float(m) for m in x]
        # x is an array/vector of floats
        total=[m**2 for m in x]
        x=init.divide(x,sum(total))
    #---------------------------------------------#
    y=matmult.matmult(arr_transpose,x)
    y=[float(i) for i in y]
    #---------------------------------------------#
    final=[matmult.dp(y,i) for i in arr]
    final.append(matmult.dp(y,in_arr))
    final_in=matmult.dp(y,in_arr)
    return matmult.result(final, final_in)
print main("/Users/sankalpyohanramesh/Google Drive/numset/testset/I1.png")
