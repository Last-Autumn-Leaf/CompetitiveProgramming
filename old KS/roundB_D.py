import math
from functools import reduce

GetIthDigit = lambda N, digit_index: int(str(N)[digit_index])
CountDigits = lambda N: len(str(N))


def CountInterestingIntegers(N):
    if N == 0: return 0;
    count = 0
    for L in range(1, len(str(N))):
        count += CountInterestingIntegersWithNumberOfDigits(L)
    count += CountInterestingIntegersWithPrefixOfN(N, P=1, S=0, digit_index=0, is_first_digit=True)
    return count


def CountInterestingIntegersWithNumberOfDigits(L):
    count = 0
    for digit in range(1, 10):
        count += f1(L - 1, P=digit, S=digit)
    return count


def CountInterestingIntegersWithPrefixOfN(N, P, S, digit_index, is_first_digit):
    if digit_index == len(str(N)):
        return 1 if S > 0 and P % S == 0 else 0
    if is_first_digit:
        digit_start = 1
    else:
        digit_start = 0

    count = 0
    for digit in range(digit_start, GetIthDigit(N, digit_index)):
        count += f1(CountDigits(N) - digit_index - 1, P * digit, S + digit)
    count += CountInterestingIntegersWithPrefixOfN(N,
                                                   P * GetIthDigit(N, digit_index),
                                                   S + GetIthDigit(N, digit_index),
                                                   digit_index + 1,
                                                   is_first_digit=False)

    return count


hashTable = dict()


def f1(L, P, S):
    if L == 0:
        return 1 if P % S == 0 else 0
    if (L, P, S) in hashTable:
        return hashTable[(L, P, S)]
    sum = 0
    for digit in range(0, 10):
        sum += f1(L - 1, P * digit, S + digit)

    hashTable[(L, P, S)] = sum
    return sum


def solve_2(A, B):
    return CountInterestingIntegers(B) - CountInterestingIntegers(A - 1)




def solve(A, B):
    counter = 0
    for i in range(A, B + 1):
        a = str(i)
        product = 1
        sum = 0
        for letter in a:
            letter = int(letter)
            product *= letter
            sum += letter
        if product % sum == 0:
            counter += 1
    return counter

hashTable_2=dict()
#return the number of interesting number between 1 and N
def f2(N):
    if N ==0 :
        return 0

    if N in hashTable_2 :
        return hashTable_2[N]
    else :
        count=0
        for Ni in range(1,N+1):

            if Ni in hashTable_2 :
                count+=hashTable_2[Ni]
            else :
                sum = 0
                prod = 1
                for  digit in str(Ni) :
                    digit=int(digit)
                    sum+=digit
                    prod*=digit
                if prod%sum==0 :
                    count+=1
                    hashTable_2[Ni]


enumDigits= lambda number : [number // 10**i % 10 for i in range(len(str(number)))]

def brute_force(A,B):
    count=0
    for i in range(A,B+1):
        sum,prod=0,1
        for d in enumDigits(i):
            sum += d
            prod *= d
        count += (prod % sum==0)
    return count

HashAttempt=dict()
def almostBruteForce(A,B):
    count=0
    for i in range(A,B+1):
        if i in HashAttempt :
            count+=HashAttempt[i]
        else :

            sum,prod=0,1
            for d in enumDigits(i):
                sum += d
                prod *= d
            count += (prod % sum==0)
            HashAttempt[i]=(prod % sum==0)
    return count


reads = lambda: [int(i) for i in input().split(' ')]

def main():
    # inputs
    T = int(input())

    for i in range(T):
        A, B = reads()
        print('Case #' + str(i + 1) + ': ' + str(almostBruteForce(A, B)))


if __name__ == '__main__':
    main()
