
def checkPalindrome(S):
    for i in range(int(len(S)/2)) :
        if S[i] != S[-(i+1)]:
            return  False
    return True

def solve(S,N):
    if N<5 :
        return  'POSSIBLE'




    for i in range(N-4) :
        current_S=S[i:i+5]


        if '?' not in S[i:i+5] and  checkPalindrome(S[i:i+5]):
            return 'IMPOSSIBLE'

    memo = dict()



def main():
    #inputs
    T= input()

    for i in range(T):
        N=input()
        S=input()

        print('Case #'+str(i+1)+': '+str(solve(S,N)))




if __name__=='__main__' :

    main()