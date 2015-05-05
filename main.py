import modules
import init
import matmult
import pickle
class Init(object):
    def __init__(self, *images):
        self.arr=[init.init(str(i)) for i in images[0]]
    def recognize(self, input_file):
        arr_transpose=matmult.transpose(self.arr)
        val=matmult.matmult(self.arr, arr_transpose)
        in_arr=init.init(input_file)
        in_arr=[float(i) for i in in_arr]
        x=[0 for i in range(len(self.arr)-1)]
        x.append(1) # x is a random unit vector
        for i in range(0,3):
            x=matmult.matmult(val, x)
            x=[float(m) for m in x]
            # x is an array/vector of floats
            total=[m**2 for m in x]
            try:
                x=init.divide(x,sum(total)) # error ocurred here, so let us debug
            except:
                x=init.divide(x,1)
        y=matmult.matmult(arr_transpose,x)
        y=[float(i) for i in y]
        final=[matmult.dp(y,i) for i in self.arr]
        final.append(matmult.dp(y,in_arr))
        final_in=matmult.dp(y,in_arr)
        output=matmult.result(final, final_in)
        return images[final.index(final[output])]
