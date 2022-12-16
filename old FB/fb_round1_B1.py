import math
import time
MOD =10e8 +7
class solution :

    def solve(self,f):
        readsfile = lambda: [int(i) for i in f.readline().split(' ')]

        N = int(f.readline())
        #Trees locations :
        trees=[]
        for i in range(N):
            A,B =readsfile()
            trees.append((A,B))
        # well locations
        wells=[]
        Q = int(f.readline())
        for i in range(Q):
            X,Y = readsfile()
            wells.append((X,Y))

        # Complexity N*Q
        ans=0

        for x,y in wells :
            for a,b in trees :
                ans += distance(x,y,a,b)
        return str(int(ans % MOD))


memoization=dict()
def distance(x,y,a,b) :
    if (x,y,a,b) not in memoization :
        memoization[(x,y,a,b)] = euclidian_d(x,y,a,b)

    return memoization[(x,y,a,b)]

euclidian_d= lambda  x,y,a,b :  (x-a)**2 + (y-b)**2
reads = lambda: [int(i) for i in input().split(' ')]

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
from bisect import bisect_right, bisect_left
def main():
    start_time = time.time()
    filename= "watering_well_chapter_1_input.txt"
    f = open(filename, "r")
    response= open(filename.replace("input","solution2"), "w")
    T = int( f.readline() )

    sol = solution()

    for test_no in range(1,T+1) :

        #print("Case #%d:" % test_no, end=" ")
        response.write("Case #%d:" % test_no +" "+ sol.solve(f)+"\n" )

    print("--- %s seconds ---" % round(time.time() - start_time, 2))

if __name__ == '__main__':
    main()

