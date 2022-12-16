import bisect
from bisect import bisect_right, bisect_left


def solve_sort():
    N =input()
    R = reads()
    sorted_index={k:i for i,k in enumerate(sorted(range(len(R)), key=R.__getitem__))}
    R_sorted=[R[i] for i in sorted_index]
    ans=[]
    for i,Ri in enumerate(R):
        ii=sorted_index[i]
        ans.append(helper(Ri,R_sorted[:ii]+R_sorted[ii+1:]))
    for anss in ans:
        print(anss, end=" ")
    print('')


def helper(Ri,R_sorted):
    return find_le_(R_sorted,2*Ri)

def find_le_(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    return -1

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

def main():


    T = int( input() )


    for test_no in range(1,T+1) :

        print("Case #%d:" % test_no, end=" ")
        solve_sort()


if __name__ == '__main__':
    main()

