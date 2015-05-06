import modules
import init
import matmult
import pickle
class Init(object):
    def __init__(self):
        self.arr=[[0,1,0,0,1,0,0,1,0], [0,0,0,1,1,1,0,0,0], [1,0,1,0,0,0,1,0,1]]
    def recognize(self, input_file):
        arr_transpose=matmult.transpose(self.arr)   
        val=matmult.matmult(self.arr, arr_transpose)
        in_arr=input_file
        in_arr=[float(i) for i in in_arr]
        x=[0 for i in range(len(self.arr)-1)]
        x.append(1)
        for i in range(0,50):
            x=matmult.matmult(val, x)
            x=[float(m) for m in x]
            total=[m**2 for m in x]
            x=init.divide(x,sum(total))
        y=matmult.matmult(arr_transpose,x)
        y=[float(i) for i in y]
        final=[matmult.dp(y,i) for i in self.arr]
        final.append(matmult.dp(y,in_arr))
        final_in=matmult.dp(y,in_arr)
        output=matmult.result(final, final_in)
        return self.arr[final.index(final[output])]
obj=Init()
print obj.recognize([0,0,0,0,1,1,0,0,0])
