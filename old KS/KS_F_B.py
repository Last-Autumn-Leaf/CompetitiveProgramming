from collections import defaultdict, deque


class solution :

    def solve(self,f=None):
        #readsfile = lambda: [int(i) for i in f.readline().split(' ')]
        N,Q = reads()

        mape = defaultdict(set)

        listOfN=[reads() for i in range(N-1)]

        q = deque()
        q.append(1)
        listOfN_ = listOfN.copy()
        while (len(q)!=0):
            current=q.popleft()
            listOfN=listOfN_.copy()
            for index, (i, j) in enumerate(listOfN):  # find first level
                if i == current:
                    mape[current].add(j)
                    listOfN_.remove([i, j])
                    q.append(j)
                elif j == current:
                    mape[current].add(i)
                    listOfN_.remove([i, j])
                    q.append(i)

        floor_list=[1,len(mape[1])]
        q = deque()
        q.append(mape[1])
        while (len(q) != 0):
            current=q.popleft()
            ans=0
            next=[]
            for child in current :
                ans+=len(mape[child])
                next+=mape[child]
            if ans :
                floor_list.append(ans)
            else : break
            if next :
                q.append(next)
            else : break


        list_of_Queries =[ int(input()) for i in range(Q)]

        ans=0
        for c in floor_list :
            if Q<c :
                return print(ans)
            else :
                Q-=c
                ans+=c
        print(ans)



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

