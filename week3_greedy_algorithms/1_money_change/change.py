# Uses python3
import sys

def get_change(m):
    #write your code here
    coin_10 = m//10
    coin_1 = m%5
    if(m - coin_10*10 - coin_1*1 == 0):
    	coin_5 = 0
    else:
    	coin_5 = 1
    return coin_10 + coin_5 + coin_1

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
