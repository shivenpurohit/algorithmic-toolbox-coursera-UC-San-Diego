#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0
    
    while(len(a) > 0):
        max_a = 0
        max_b = 0
        for i in range(len(a)):
            if(a[i] > a[max_a]):
                max_a = i
            if(b[i] > b[max_b]):
                max_b = i    
        res += a[max_a] * b[max_b]
        
        del a[max_a:max_a+1]
        del b[max_b:max_b+1]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
