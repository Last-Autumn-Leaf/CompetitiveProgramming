def solve():
    N,K = reads()
    S= reads()
    map={}
    st=set()

    if 2*K < N :
        return print('NO')
    for s in S :
        map[s]=map.get(s,0) +1
        st.add(s)

        if map[s] >2 : # duplicate case
            return print('NO')
        if len(st) > 2*K : # can't display everystyle
            return print('NO')

    print('YES')







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


    T = int( input() )


    for test_no in range(1,T+1) :

        print("Case #%d:" % test_no, end=" ")
        solve()



if __name__ == '__main__':
    main()

