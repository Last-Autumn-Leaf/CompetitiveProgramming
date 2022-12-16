from collections import defaultdict, deque


class solution :

    def knapSack(self,W, wt, val, n):
        dp = [0 for i in range(W + 1)]  # Making the dp array

        for i in range(1, n + 1):  # taking first i elements
            for w in range(W, 0, -1):  # starting from back,so that we also have data of
                # previous computation when taking i-1 items
                if wt[i - 1] <= w:
                    # finding the maximum value
                    dp[w] = max(dp[w], dp[w - wt[i - 1]] + val[i - 1])

        return dp[W]  # returning the maximum value of knapsack


    def solve(self,f=None):
        #readsfile = lambda: [int(i) for i in f.readline().split(' ')]
        D,N,X = reads()
        val=[]
        wt=[]
        W= D*X

        for i in range(N):
            Q,L,V = reads()
            for j in range(Q):
                val.append(V)
                wt.append(L)
        n = len(val)
        print(self.knapSack(W, wt, val, n))




def max_min(val,max_v,min_v):
    return max(min(val,max_v),min_v)

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

    a=solution()
    for test_no in range(1,T+1) :

        print("Case #%d:" % test_no, end=" ")
        a.solve()




if __name__ == '__main__':
    main()

