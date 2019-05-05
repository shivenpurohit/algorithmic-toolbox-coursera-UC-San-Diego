# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    m=1
    while(m*(m+1)/2 <= n):
    	m+=1
    m = m-1

    for i in range(m-1):
    	summands.append(i+1)
    summands.append(int(n - m*(m-1)/2))
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
