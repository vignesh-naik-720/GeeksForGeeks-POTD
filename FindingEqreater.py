"""
Our friend John has given us an array consisting of N integers. In each question John has given Bob a value X, to find an element Ai in the array which is either greater than or equal to X and such that the difference between Ai and X is as small as possible.

John will ask Bob Q such questions, and we need to help Bob answer them.

Note: Use fast i/o for the given problem.

Input Format
The first line contains t (1≤ t ≤100), the number of test cases.
The first line of each test case contains a single integer n (1≤n≤2⋅10^5) — the number of elements in the array.
The second line contains n integers a1,a2,…,an  (1 ≤ ai ≤10^9) — the initial value of element ai  
The Third line of each test case contains a single integer q (1≤q≤2⋅10^5) — the number of queries.
Then the following each q line contains a query, the value X.
The sum of n over all test cases doesn't exceed 2*10^5.

Output Format
Return a single integer Ai for each Query such that if Z =  Ai – X, then Z >= 0 and Z is minimized; if there does not exist any such integer, then return -1.
Constraints
1 <= T <= 100
1 <= N <= 2e^5
1 <=Q <= 2e^5
Sample Testcase 0
Testcase Input
2 
3
1 5 4
2 
1 
2
2 
1 6
1 
3
Testcase Output
1
4
6
Explanation
Test case 1:



For X = 1, we have A1 = 1, (A1-X) is the minimum possible difference possible which is zero.

For X = 2, we have A3 = 4, (A3-X) is the minimum possible difference possible which is two.


Test case 2:


For X = 3, we have A2 = 6, (A2-X) is the minimum possible difference possible which is three.

Sample Testcase 1
Testcase Input
1   
5
3 2 1 5 4
3
1
2
6
Testcase Output
1
2
-1
Explanation
Test case 1:



For X = 1, we have A3 = 1, (A3-X) is the minimum possible difference possible which is zero.

For X = 2, we have A2 = 2, (A2-X) is the minimum possible difference possible which is zero.

For X = 6, we don’t have a number greater than or equal to X present in the array.
"""
def user_logic(n, arr, q, queries):
    """
    Write your logic here.
    Parameters:
        n (int): Number of elements in the array
        arr (list): List of integers representing the array
        q (int): Number of queries
        queries (list): List of integers representing the queries
    Returns:
        list: List of integers representing the results for each query
    """
    import bisect

    # Sort the array for binary search
    arr.sort()

    results = []
    for x in queries:
        # Use binary search to find the smallest number >= x
        pos = bisect.bisect_left(arr, x)
        if pos < n:
            results.append(arr[pos])
        else:
            results.append(-1)

    return results

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        q = int(data[index])
        index += 1
        queries = list(map(int, data[index:index + q]))
        index += q
        
        # Call user logic function
        result = user_logic(n, arr, q, queries)
        results.extend(result)
    
    # Print all results for each query in each test case
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
