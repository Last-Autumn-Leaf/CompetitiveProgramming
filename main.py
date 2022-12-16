from collections import defaultdict

MOD=10**9+7*(1000000007)


class solution :
    memo={}
    def solve(self,f=None):
        self.A,self.B,N,K=reads()

        ans=0
        for i in range(1,N+1):
            for j in range(1,N+1):
                if i ==j :
                    ...
                else:
                    if (i**self.A +j**self.B)%K==0 :
                        ans+=1
        return print(ans %MOD)

    def helper(self,i,j):



def ForceInput(type=int) :
    while True:
        s = input()
        if s:
            break
    return s

reads = lambda type=int: list(map(type, input().split()))
createMap= lambda R,C,val=False :   [[val for i in range(C)] for j in range(R)]

def main():

    #f = open("second_second_friend_sample_input.txt", "r")
    T = int( input() )


    for test_no in range(1,T+1) :

        print("Case #%d:" % test_no, end=" ")
        solution().solve()




if __name__ == '__main__':
    main()

