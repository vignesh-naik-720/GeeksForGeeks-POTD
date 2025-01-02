'''
In a quiet village, a boy named Arjun found an old diary hidden in his grandmother’s trunk. The diary was filled with random letters and numbers, and a note inside read:

"Hidden within this diary are Fibonacci numbers—unlock their secrets to discover something extraordinary."

Arjun had heard of Fibonacci numbers before. They were a special sequence where each number was the sum of the two before it, starting from 0 and  1. Excited by the challenge, he decided to find these numbers.

His task was clear:

Search the diary and count how many Fibonacci numbers were hidden within.
Write down all the Fibonacci numbers he found.
Finally, list the first K Fibonacci numbers starting from 0, where K is the total count of numbers he found in the diary.
If there were no Fibonacci numbers, Arjun would close the diary and look elsewhere for his adventure.

With a curious mind and a pencil in hand, Arjun began his search. Would he uncover the Fibonacci sequence hidden in the diary, or was it just an old book with random scribbles?

Input Format
The first line of input contains a string ‘S’ consisting of lowercase English letters and digits(1-9).

Output Format
If Fibonacci numbers are present in the string:

Print the count of Fibonacci numbers.
Print the identified Fibonacci numbers found in the string.
Print the first k Fibonacci numbers starting from 0 where K is the count of Fibonacci numbers found in the string.
If no Fibonacci numbers are found, print 0.

Constraints
1 <= length(S) <= 10^2

Sample Testcase 0
Testcase Input
a1b13c2d8e21
Testcase Output
5
1 13 2 8 21
0 1 1 2 3
Explanation
Extracted Numbers from string: [1, 13, 2, 8, 21]
Fibonacci Series: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, . . . 


Identified Fibonacci Numbers: [1, 13, 2, 8, 21]
Count Fibonacci Numbers: 5
First 8 Fibonacci numbers: 0, 1, 1, 2, 3.

Sample Testcase 1
Testcase Input
a1b34cd2f7ghi1ch2v34
Testcase Output
6
1 34 2 1 2 34
0 1 1 2 3 5
Explanation
Extracted Numbers from string: [1, 34, 2, 7, 1, 2, 34]
Fibonacci Series: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, . . . 


Identified Fibonacci Numbers: [1, 34, 2, 1, 2, 34]
Count Fibonacci Numbers: 6
First 3 Fibonacci numbers: 0, 1, 1, 2, 3, 5.
'''
def optimal_fibonacci_count(s):
    # Function to be implemented by the user
    def generate_fibonacci(limit):
        fib_list = []
        a, b = 0, 1
        for _ in range(limit):
            fib_list.append(a)
            a, b = b, a + b
        return fib_list
    import re
    numbers = list(map(int, re.findall(r'\d+', s)))

    if not numbers:
        print(0)
        return ""

    fib_numbers = []
    fib_set = set()
    a, b = 0, 1
    while a <= max(numbers):
        fib_set.add(a)
        a, b = b, a + b
    for num in numbers:
        if num in fib_set:
            fib_numbers.append(num)

    if not fib_numbers:
        print(0)
        return ""
    
    k = len(fib_numbers)
    print(k)
    print(' '.join(map(str, fib_numbers)))
    return(' '.join(map(str, generate_fibonacci(k))))
    

if __name__ == '__main__':
    s = input().strip()
    print(optimal_fibonacci_count(s))
