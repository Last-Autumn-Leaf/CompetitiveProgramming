def solve():
    N = int(input())
    P=input()
    x=1
    while(x<N):
        if(isPalindrome(P[0:x]) and isPalindrome(P[x:N])):
            print(P[0:x])
            break
        x+=1
    if x==N : print(P)


def isPalindrome(s):
    return s == s[::-1]


reads = lambda: [int(i) for i in input().split(' ')]
def main():


    T = int( input() )


    for test_no in range(1,T+1) :

        print("Case #%d:" % test_no, end=" ")
        solve()



if __name__ == '__main__':
    main()

