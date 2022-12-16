
special_char='#@*&'

def solve(N):
    lower=False
    upper=False
    digit=False
    special=False
    for n in N :
        if upper or n.isupper():
            upper=True
        if lower or n.islower():
            lower=True
        if digit or n.isdigit():
            digit=True
        if special or n in special_char :
            special=True
        if upper and lower and digit and special :
            break

    if not upper :
        N+='A'
    if not lower :
        N+='a'
    if not digit :
        N+='1'
    if not special :
        N+='#'
    while(len(N)<7):
        N+='1'

    return N


def main():

    # ------ Récupérer les inputs ------

    # test case T
    T = int( input() )


    for i in range(T) :
        input()
        N = input()

        print('Case #'+str(i+1)+': '+str(solve(N)))



if __name__ == '__main__':
    main()
