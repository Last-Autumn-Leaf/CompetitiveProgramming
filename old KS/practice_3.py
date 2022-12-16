


N,S,E,W='N','S','E','W'
dirs={
    N:(-1,0),
    S:(1,0),
    E:(0,1),
    W:(0,-1)
}
class solution :

    def solve(self,f=None):
        #readsfile = lambda: [int(i) for i in f.readline().split(' ')]
        NbOfI,R,C,Sr,Sc =reads()
        instrucstions=input()
        carte={}
        Sr-=1
        Sc-=1
        current_dir=(0,0)
        for ins in instrucstions :
            while(Sr in carte and Sc in carte[Sr]):
                Sr+=current_dir[0]
                Sc+=current_dir[1]

            if Sr in carte :
                carte[Sr].add(Sc)
            else:
                carte[Sr]={Sc}
            current_dir=dirs[ins]
            Sr+=current_dir[0]
            Sc+=current_dir[1]

        while(Sr in carte and Sc in carte[Sr]):
            Sr += current_dir[0]
            Sc += current_dir[1]

        print(Sr+1,Sc+1)




reads = lambda type=int: map(type, input().split())
createMap= lambda R,C,val=False :   [[val for i in range(C)] for j in range(R)]

def main():

    #f = open("second_second_friend_sample_input.txt", "r")
    T = int( input() )


    for test_no in range(1,T+1) :

        print("Case #%d:" % test_no, end=" ")
        solution().solve()



if __name__ == '__main__':
    main()

