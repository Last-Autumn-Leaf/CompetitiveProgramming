from collections import defaultdict


class solution :

    def solve(self,f=None):
        #readsfile = lambda: [int(i) for i in f.readline().split(' ')]
        N=ForceInput()
        AB=reads()

        P= int(input())
        C=[]
        for i in range(P):
            C.append(int(input()))
        maxC,minC=max(C),min(C)



        freq={}
        freq=defaultdict(lambda: 0, freq)
        # pré-traitement des données
        for i in range(0,len(AB),2):
            A=AB[i]
            B=AB[i+1]
            if(B<minC or A >maxC):
                ...
            else :
                A=max_min(A,maxC,minC)
                B=max_min(B,maxC,minC)
                for j in range(A,B+1):
                    freq[j]+=1



        for ci in C :
            print(freq[ci],end=' ')
        print('')


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


    for test_no in range(1,T+1) :

        print("Case #%d:" % test_no, end=" ")
        solution().solve()




if __name__ == '__main__':
    main()

