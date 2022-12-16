import math

EPS = 10e-6
AREA=lambda r: math.pi*r**2
def solve(R,A,B):
    area_sum=AREA(R)
    new_R=R
    while(True) :
        #Left
        new_R = A*new_R
        area_sum+=AREA(new_R)
        new_R =  int(new_R / B)
        if new_R==0 :
            break;
        else :
            area_sum += AREA(new_R)
    return round(area_sum,6)




def main():
    #inputs
    T= int(input())

    for i in range(T):
        R,A,B=[int(i) for i in input().split(' ')]


        print('Case #'+str(i+1)+': '+str(solve(R,A,B)))




if __name__=='__main__' :

    main()