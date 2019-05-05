#Uses python3

import sys

def isMaxNum(x,max_num):
	num1 = str(x)+str(max_num)
	num2 = str(max_num)+str(x)

	if(int(num1) > int(num2)):
		return True
	else:
		return False

def largest_number(a):
    #write your code here
    res = ""
    c=0
    while(len(a)>0):
    	max_num =0
    	for x in a:
    		if(isMaxNum(x,max_num)):
    			max_num = x
    	res += str(max_num)
    	a.remove(max_num)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
