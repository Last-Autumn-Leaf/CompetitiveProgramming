# USEFULL MACROS:

    typedef long long ll;
    typedef pair<int,int> pii;
    typedef pair<int,pii> p3;
    typedef pair<ll,ll> pl;
    typedef pair<int,pl> p3l;
    typedef pair<double,double> pdd;
    typedef vector<int> vi;
    typedef vector<ld> vd;
    typedef unordered_map<int,int> mii;
     
    #define FOR(i,a,b) for(int i=(a);i<(b);i++)
    #define REP(i,n) FOR(i,0,n)
    #define SORT(v) sort((v).begin(),(v).end())
    #define UN(v) SORT(v),(v).erase(unique((v).begin(),(v).end()),(v).end())
    #define CL(a,b) memset(a,b,sizeof a)
    #define pb push_back


# SORT A VECTOR:
    sort( values.begin( ), values.end( ), [ ]( const auto& lhs, const auto& rhs )
    {
      return lhs.key < rhs.key;
    });


# priority queue :
    auto comp = [&](const pair<string,int>& a, const pair<string,int>& b) {
               return a.second > b.second || (a.second == b.second && a.first < b.first);
           };
    priority_queue<pair<int, string>, vector<pair<int, string>>, decltype(comp)> q(comp);
    
    #----- by struct
    struct Compare {
    bool operator() (pair<int, string> a, pair<int, string> b) {
        if(a.first == b.first)
            return a.second > b.second;
        else
            return a.first < b.first;
    }
    };

    priority_queue<pair<int, string>, vector<pair<int, string>>, Compare> q;

# QUEUE :
    //include <queue>

    queue<string> languages;
    languages.empty()
    languages.push("Python");
    languages.front();
    languages.pop();
      

# STACK :
    stack<int> stack;
    stack.push(21);
    stack.top()
    stack.pop();
    stack.empty();


# initialize a 2d vector :

    int m = 2, n = 5;
    vector<vector<int>> vec(m, vector<int> (n, 0));


# binary search 
    auto it = lower_bound(sub.begin(), sub.end(), x); // Find the index of the first element >= x
                    *it = x; // Replace that number with x

# Prime factors :
    void primeFactors(int n) { 
        // Print the number of 2s that divide n 
        while (n%2 == 0) 
        { 
            printf("%d ", 2); 
            n = n/2; 
        } 
     
    // n must be odd at this point.  So we can skip  
    // one element (Note i = i +2) 
    for (int i = 3; i <= sqrt(n); i = i+2) 
    { 
        // While i divides n, print i and divide n 
        while (n%i == 0) 
        { 
            printf("%d ", i); 
            n = n/i; 
        } 
    } 
     
    // This condition is to handle the case when n  
    // is a prime number greater than 2 
    if (n > 2) 
        printf ("%d ", n); 

# cardinals neighbours :
    vector<vector<int> > dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

# Quick Select :
    bool myfunction (int i,int j) { return (i<j); }
    nth_element (myvector.begin(), myvector.begin()+5, myvector.end(),myfunction);
    // OR using using [] function
    nth_element(A.begin(), A.begin() + K, A.end(), [](vector<int>& a, vector<int>& b) {
            return a[0] * a[0] + a[1] * a[1] < b[0] * b[0] + b[1] * b[1];
        });

# Sieve of Eratosthenes (find prime numbers):
    vector<bool> prime(n + 1, true);
    prime[0] = false;
    prime[1] = false;
    for (int i = 2; i * i <= n; i++) {
        if (prime[i]) {
            for (int j = i * i; j <= n; j += i) {
                prime[j] = false;
            }
        }
    }


# Union find :
    public:
    int par[26];
    
    int find(int x){
        if(par[x]==-1) return x;
        return par[x]=find(par[x]);
    }
    
    void Union(int x, int y) {
        x = find(x);
        y = find(y);
        
        if (x != y) 
            par[x] = y; 
    }

