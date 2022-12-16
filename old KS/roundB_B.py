import math
from functools import reduce

def rev(num):
    return int(num != 0) and ((num % 10) * \
             (10**int(math.log(num, 10))) + \
                          rev(num // 10))

def factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if (n % i == 0  ))
                      )
               )
EPS = 10e-6

def solve(A):
    sum=0
    for num in factors(A):
        if num==rev(num):
            sum+=1
    return sum




def main():
    #inputs
    T= int(input())

    for i in range(T):
        A=int(input())


        print('Case #'+str(i+1)+': '+str(solve(A)))




if __name__=='__main__' :

    main()