import re

TREE='^'
SPACE='.'
ROCK='#'
class solution :

    def solve(self,f):
        readsfile = lambda: [int(i) for i in f.readline().split(' ')]

        self.R,self.C = readsfile()
        self.map=[] # dim = R*C
        self.visited=[[False for i in range(self.C)] for j in range(self.R)]
        for i in range (self.R):
            #ci=re.split('. |^')
            self.map.append(list(f.readline().replace('\n','')))

        for i in range(self.R):
            for j in range(self.C):

                if(self.map[i][j]==TREE and self.isLonely(i,j) and not self.visited[i][j]) :
                    self.visit(i,j)
        ss=''
        for i in range(self.R):
            ss+=''.join(self.map[i])+'\n'
            for j in range(self.C):
                if(self.map[i][j]==TREE and self.isLonely(i,j)) :
                    return print('Impossible')
        print('Possible')
        return print(ss)

    def visit(self,i,j):
        if self.visited[i][j] :return
        self.visited[i][j]=True
        valid_neigh=self.get_Valid_neighbor(i,j)

        if len(valid_neigh)==0 :
            return self.isLonely(i,j) # return true if no valid path found
        for ii,jj in valid_neigh:
            if self.validCell(ii,jj) :#and self.isLonely(ii,jj):
                if (self.map[ii][jj]) == TREE :
                    resp=self.visit(ii,jj)
                else :
                    self.map[ii][jj] = TREE
                    resp = self.visit(ii, jj)
                    if (resp) :
                        self.map[ii][jj] =SPACE


    def isLonely(self,i,j): # is Lonely if it has less than two trees as neighbor
        ans=self.get_Valid_neighbor(i,j)
        nmbrOfTrees=0
        for i,j in ans:
            if self.map[i][j]==TREE:
                nmbrOfTrees+=1
        return nmbrOfTrees <2

    def validCell(self,i,j): # is Valid if it has at least two empty or tree cells
        return len(self.get_Valid_neighbor(i,j)) >= 2

    def get_Valid_neighbor(self,i,j): # doesn't work on a rock
        # return a list of non-rocked cases
        if self.notValid(i,j): return []
        ans=[]
        if not self.notValid(i-1,j) : ans.append((i-1,j))
        if not self.notValid(i+1,j) : ans.append((i+1,j))
        if not self.notValid(i,j-1) : ans.append((i,j-1))
        if not self.notValid(i,j+1) : ans.append((i,j+1))
        return ans


    def notValid(self,i,j):
        return   i<0 or i>= self.R or j<0 or j>=self.C or self.map[i][j]==ROCK

reads = lambda: [int(i) for i in input().split(' ')]

def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
from bisect import bisect_right, bisect_left
def main():

    f = open("second_second_friend_sample_input.txt", "r")
    T = int( f.readline() )


    for test_no in range(1,T+1) :

        print("Case #%d:" % test_no, end=" ")
        solution().solve(f)



if __name__ == '__main__':
    main()

