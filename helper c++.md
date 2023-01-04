
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