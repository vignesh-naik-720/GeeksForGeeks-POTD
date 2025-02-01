"""
You are given a two-dimensional mat[][] of size n*m containing English alphabets and a string word. Check if the word exists on the mat. The word can be constructed by using letters from adjacent cells, either horizontally or vertically. The same cell cannot be used more than once.

Examples :

Input: mat[][] = [['T', 'E', 'E'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: true
Explanation:

The letter cells which are used to construct the "GEEK" are colored.
Input: mat[][] = [['T', 'E', 'U'], ['S', 'G', 'K'], ['T', 'E', 'L']], word = "GEEK"
Output: false
Explanation:

It is impossible to construct the string word from the mat using each cell only once.
Input: mat[][] = [['A', 'B', 'A'], ['B', 'A', 'B']], word = "AB"
Output: true
Explanation:

There are multiple ways to construct the word "AB".
Constraints:
1 ≤ n, m ≤ 100
1 ≤ L ≤ n*m
"""
def isWordExist(self, mat, word):
		n, m = len(mat), len(mat[0])
        def dfs(x, y, index):
            if index == len(word):  # If all characters of the word are matched
                return True
            if x < 0 or y < 0 or x >= n or y >= m or mat[x][y] != word[index]:  
                return False
            temp, mat[x][y] = mat[x][y], '#'  # Mark the cell as visited
            # Explore all 4 possible directions: up, down, left, right
            found = (dfs(x + 1, y, index + 1) or 
                     dfs(x - 1, y, index + 1) or 
                     dfs(x, y + 1, index + 1) or 
                     dfs(x, y - 1, index + 1))
            
            mat[x][y] = temp  # Restore the cell
            return found

        for i in range(n):
            for j in range(m):
                if mat[i][j] == word[0]:  # Start DFS from each cell matching the first letter
                    if dfs(i, j, 0):
                        return True

        return False
