def solve():
    N = int(input())

    ans=0
    while(N>0):
        ans+=1
        N-=5
    print(ans)


reads = lambda: [int(i) for i in input().split(' ')]
def main():

    T = int( input() )
    for test_no in range(1,T+1) :
        print("Case #%d:" % test_no, end=" ")
        solve()



if __name__ == '__main__':
    main()

