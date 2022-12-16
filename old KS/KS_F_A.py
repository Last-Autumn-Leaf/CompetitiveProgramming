from collections import defaultdict

class solution :

    def solve(self,f=None):
        #readsfile = lambda: [int(i) for i in f.readline().split(' ')]
        N = int(input())

        def sort_byC(elem):
            return elem[0],int(elem[2])

        def sort_byD(elem):
            return int(elem[1]),int(elem[2])


        fabrics_list=[input().split(' ') for i in range(N)]
        Ada=sorted(fabrics_list, key=sort_byC)
        Charles=sorted(fabrics_list, key=sort_byD)
        ans=0
        for x,y in zip(Ada,Charles):
            if x==y :
                ans+=1
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

