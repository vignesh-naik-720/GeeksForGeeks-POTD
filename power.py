"""
Implement the function power(b, e), which calculates b raised to the power of e (i.e. be).
Examples:
Input: b = 3.00000, e = 5
Output: 243.00000
Input: b = 0.55000, e = 3
Output: 0.16638
Input: b = -0.67000, e = -7
Output: -16.49971
Constraints:
-100.0 < b < 100.0
-10^9 <= e <= 10^9
Either b is not zero or e > 0.
-10^4 <= b^e <= 10^4
"""
def power(self, b: float, e: int) -> float:
        # Using Python's built-in power function for efficiency
        result = pow(b, e)
        # Rounding to 5 decimal places as per examples
        return round(result, 5)
