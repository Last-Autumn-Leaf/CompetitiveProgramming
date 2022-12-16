import math

EPS = 10e-6

def normZero(Vi:int,D:int):
    return min(Vi,D-Vi)


def distBetweenTwoNumber(A,B,D):
    return min(abs(A-B), D-abs(B-A))

def findNumBorder(V:list,Number=0):
    i,j=0,len(V)-1;

    while(i!=j and i < j) :
        if V[i] ==Number :
            i+=1
        if V[j]==Number :
            j-=1
        if V[j]!=Number and V[i] !=Number :
            break;
    return i,j

def findUtilBorders(V:list,A,B,i,j):


    while(i!=j and i < j) :
        if V[i+1] ==A :
            i+=1
        if V[j-1]==B :
            j-=1
        if V[i+1]!=A and V[j-1] !=B :
            break;
    return i,j



def solve(N,D,V):
    #print(N,'dials of size :',D)
    #print(V)
    i,j=findNumBorder(V)
    if (i == j ) :
        return normZero(V[j], )
    elif  i > j :
        # Full of zeros
        return 0
    else :
        V=V[i:j+1]

    i, j = 0, len(V) - 1;
    sumOfOperations=0
    sameArray=False

    # first op :
    i, j = findUtilBorders(V, V[i], V[j], i, j)
    if i == j or i > j :
        return normZero(V[i],D)
    else :
        if normZero(V[i],D) < normZero(V[j],D) :
            sumOfOperations += normZero(V[i],D)
            i+=1
        else :
            sumOfOperations += normZero(V[j],D)
            j-=1



    while(i != j or i < j):

        i,j= findUtilBorders(V,V[i],V[j],i,j)
        if i==j :
            # END OF OPERATIONS
            sumOfOperations+=normZero(V[i], D)
            sameArray=True;
            break;

        #Égaux
        if V[i]==V[j]:
            sumOfOperations+=normZero(V[i], D)
            if i +1 != j-1 and i+1 < j-1 :
                if (normZero(V[i+1], D)) > normZero(V[j-1], D):
                    sumOfOperations += distBetweenTwoNumber(V[i+1], V[j-1], D)
                elif (normZero(V[i+1], D)) <= normZero(V[j-1], D):
                    sumOfOperations += distBetweenTwoNumber(V[i+1], V[j-1], D)
            else :
                if i +1 == j-1 :
                    sumOfOperations+=distBetweenTwoNumber(V[i],V[i+1],D)
                else :
                    ...
            i+=1
            j-=1

        elif (normZero(V[i], D))>normZero(V[j], D) :
            i+=1
            sumOfOperations+=distBetweenTwoNumber(V[i],V[j],D)
        elif (normZero(V[i], D))<=normZero(V[j], D) :
            j-= 1
            sumOfOperations += distBetweenTwoNumber(V[i], V[j], D)
    if i==j :
        sumOfOperations+= normZero(V[j], )



def solve_2(N, D, V):
        # print(N,'dials of size :',D)
        # print(V)
        i, j = findNumBorder(V)
        if (i == j):
            return normZero(V[j], )
        elif i > j:
            # Full of zeros
            return 0
        else:
            V = V[i:j + 1]

        i, j = 0, len(V) - 1;
        sumOfOperations = 0
        sameArray = False

        # first op :
        i, j = findUtilBorders(V, V[i], V[j], i, j)
        if i == j or i > j:
            return normZero(V[i], D)
        else:
            if normZero(V[i], D) < normZero(V[j], D):
                sumOfOperations += normZero(V[i], D)
                sumOfOperations += distBetweenTwoNumber(V[i], V[i + 1], D)
                i += 1
            elif normZero(V[i], D) > normZero(V[j], D):
                sumOfOperations += normZero(V[j], D)
                sumOfOperations += distBetweenTwoNumber(V[j], V[j- 1], D)
                j -= 1
            else :
                sumOfOperations += normZero(V[j], D)
                sumOfOperations += distBetweenTwoNumber(V[i], V[i + 1], D)
                #sumOfOperations += distBetweenTwoNumber(V[j], V[j- 1], D)
                i += 1
                j -= 1
        while (i != j or i < j):
            i, j = findUtilBorders(V, V[i], V[j], i, j)
            if i == j or i > j:
                # END OF OPERATIONS
                sumOfOperations += normZero(V[i], D)
                return sumOfOperations;

            if distBetweenTwoNumber(V[i],V[i+1],D) < distBetweenTwoNumber(V[j],V[j-1],D) :
                sumOfOperations+=distBetweenTwoNumber(V[i],V[i+1],D)
                i+=1
            elif distBetweenTwoNumber(V[i],V[i+1],D) >= distBetweenTwoNumber(V[j],V[j-1],D) :
                sumOfOperations += distBetweenTwoNumber(V[j], V[j-1], D)
                j-= 1

        return sumOfOperations


def currentVal(Vi,k,D):
    return (Vi - k +D) % D


def solve_3(N, D, V):
    dp = [[[-1 for k in range(2)] for j in range(N)] for i in range(N)]

    def salvation(i,j,bit):
        if i >j :
            return 0
        if dp [i][j][bit] != -1 :
            return dp[i][j][bit];

        k=0
        if not bit:
            if i >0 :
                k=D - V[i-1]

        else :
            if j < N-1 :
                k=D - V[j+1]


        currentVal_i = currentVal(V[i],k,D)
        currentVal_j = currentVal(V[j],k,D)

        currOperations = normZero(currentVal_i,D)
        val_i = currOperations + salvation(i+1,j,0)

        currOperations= normZero(currentVal_j,D)
        val_j=currOperations + salvation(i,j-1,1)

        dp[i][j][bit] = min(val_i,val_j)
        return dp[i][j][bit]

    return  salvation(0,N-1,0)






def main():
    #inputs
    T= int(input())

    for i in range(T):
        N,D=[int(i) for i in input().split(' ')]
        V=[int(i) for i in input().split(' ')]

        print('Case #'+str(i+1)+': '+str(solve_3(N,D,V)))




if __name__=='__main__' :

    main()