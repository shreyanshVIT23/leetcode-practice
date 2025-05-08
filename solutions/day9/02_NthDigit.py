class Solution:
    def findNthDigit(self, n: int) -> int:
        # Step 1: Handle single-digit case directly
        if n <= 9:
            return n
        
        # Initialize variables to determine the range
        length = 1  # Current digit length (1-digit, 2-digit, ...)
        count = 9    # Number of numbers with 'length' digits
        start = 1    # Starting number of the current range (1 for 1-digit, 10 for 2-digit, etc.)
        
        # Step 2: Find the range where 'n' falls
        while n > length * count:
            n -= length * count  # Subtract the total number of digits in the current range
            length += 1           # Increase the number of digits for the next range
            count *= 10           # There are now 10 times more numbers (10-99, 100-999, etc.)
            start *= 10           # The starting number for the next range (10, 100, 1000, etc.)
        
        # Step 3: Find the number that contains the nth digit
        number = start + (n - 1) // length  # Find the number within the current range
        digit_pos = (n - 1) % length        # Find the position of the digit within that number
        
        # Step 4: Extract and return the digit
        return int(str(number)[digit_pos])  # Convert the number to a string and return the digit


sol = Solution()
print(sol.findNthDigit(3))  # Output: 3
print(sol.findNthDigit(1002)) # Output: 0 