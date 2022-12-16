def subsetsum(array,num):

    if num == 0 or num < 1:
        return None
    elif len(array) == 0:
        return None
    else:
        if array[0] == num:
            return [array[0]]
        else:
            with_v = subsetsum(array[1:],(num - array[0]))
            if with_v:
                return [array[0]] + with_v
            else:
                return subsetsum(array[1:],num)


def solve(N,X,Y):
    S = N*(N+1)/2
    Allan=0
    Barbara=S
    while(Allan/Barbara!=X/Y):
        Allan+=1
        Barbara-=1
        if Barbara==0 :
            return 'IMPOSSIBLE'
    list_of_int=[i for i in range(1,N+1)]
    if Allan in list_of_int :
        allan_num= list_of_int.pop(list_of_int.index(Allan))
        return 'POSSIBLE\n'+'1'+'\n'+str(allan_num)

    else :
        result=subsetsum(array=list_of_int,num=Allan)
        if result is not None :
            s = 'POSSIBLE\n'+str(len(result))+'\n'
            for i in result:
                s += str(i) + ' '
            return s[:-1]

        else :
            return 'IMPOSSIBLE'



reads = lambda: [int(i) for i in input().split(' ')]
def main():

    # test case T
    T = int( input() )


    for i in range(T) :

        N,X,Y= reads()
        print('Case #'+str(i+1)+': '+str(solve(N,X,Y)))



if __name__ == '__main__':
    main()