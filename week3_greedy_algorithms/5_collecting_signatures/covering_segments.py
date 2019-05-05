# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def sortSegments(x):
    return x.start

def optimal_points(segments):
    points = []
    #write your code here
    segments=sorted(segments, key=sortSegments)
    
    count=1
    points=[]
    currentStart=None
    currentEnd=None

    for s in segments:
        if(currentStart==None and currentEnd==None):
            currentStart=s.start
            currentEnd=s.end
        else:
            if(s.start<=currentEnd):
                currentStart=s.start
                if(currentEnd>s.end):
                    currentEnd=s.end
                continue
            else:
                count+=1
                points.append(currentStart)
                currentStart,currentEnd=s.start,s.end

    points.append(currentStart)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
