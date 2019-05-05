# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    # write your code here
    while(capacity > 0 and len(weights) > 0):
    	max_index = 0
    	for i in range(1,len(weights)):
    		if(values[i]/weights[i] > values[max_index]/weights[max_index]):
    			max_index = i
    	if(weights[max_index] > capacity):
    		value+=(values[max_index]*capacity/weights[max_index])
    		capacity = 0
    	else:
    		value+=values[max_index]
    		capacity-=weights[max_index]
    	del weights[max_index:max_index+1]
    	del values[max_index:max_index+1]
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
