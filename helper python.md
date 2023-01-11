# DEFAULT DICT
	from collections import defaultdict
	d = defaultdict(def_value)


# BINARY SEARCH
	

    def binary_search(array) -> int:
    	    def condition(value) -> bool:
    	        pass #condition
    
    	    left, right = 0, len(array) # correct boundary
    	    while left < right: 
    	        mid = left + (right - left) // 2
    	        if condition(mid):
    	            right = mid
    	        else:
    	            left = mid + 1
    	    return left # (left or left-1)

# BFS (double end Queue)
	from collections import deque
	  
	q = deque()
	visited = set()

	q.append(0)
	while q:
	    start = q.popleft()
	    if start in visited:
	        continue
	    for end in range(start + 1, len(s) + 1):
	        if condition(start):
	            q.append(end)
	            if end == len(s):
	                return True
	    visited.add(start)
	return False

# Queue :
	from queue import Queue
	q = Queue(maxsize = 3)
	#put,get,empty


# BISECT :
	# Find the index of the smallest number >= x
	idx = bisect_left(sub, x)  

# CACHE LRU :
	from functools import lru_cache
	@lru_cache(None) # decorator for the function


# cardinals neighbours
	for ii,jj in ( (i+1,j),(i-1,j),(i,j+1),(i,j-1)):


# Union Find Class
	class UnionFind(object):
    def __init__(self, n):
        self.u = list(range(n))
        
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb: self.u[ra] = rb
    
    def find(self, a):
        while self.u[a] != a: a = self.u[a]
        return a

# prime factors 
	def prime_factors(n):
            ans=[]
            while (n%2 == 0) :
                ans.append(2)
                n = n/2; 

            for i in range(3,int(sqrt(n))+1,2):
                while (n%i == 0) :
                    ans.append(i)
                    n = n/i; 

            if (n > 2) : ans.append(n)
            return ans



