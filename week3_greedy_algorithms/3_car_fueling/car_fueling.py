# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    capacity = tank
    stops.append(distance)
    ans=0
    if(distance <= tank):
    	return 0
    else:
	    for i in range(len(stops)):
	    	#check feasibility
	    	if((i==0 and stops[i] > capacity) or (i>0 and stops[i] - stops[i-1] > tank)):
	    		return -1
	    	#print(capacity)
	    	if(i==0):
	    		capacity -= stops[i]
	    	else:
	    		dist = stops[i]-stops[i-1]
	    		if(capacity - dist < 0):
	    			capacity = tank - dist
	    			ans+=1
	    		else:
	    			capacity -= dist
	    		#print ('dist: ',dist)
	    		#print ('ans: ',ans)

	    return ans

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
