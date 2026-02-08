class Solution:
    def longestPalindrome(self, s: str) -> str:
        # If string is empty or has one character, it's already a palindrome
        if not s or len(s) == 1:
            return s
        
        start, end = 0, 0  # to track the bounds of the longest palindrome
        
        # Helper function to expand around the center and return palindrome length
        def expand_from_center(left: int, right: int) -> int:
            # Expand as long as left and right are in bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # When the loop ends, left and right are one step beyond the valid palindrome
            return right - left - 1  # length of the palindrome
        
        for i in range(len(s)):
            # Odd-length palindrome (center is one character)
            len1 = expand_from_center(i, i)
            # Even-length palindrome (center is between two characters)
            len2 = expand_from_center(i, i + 1)
            
            # Take the longer length
            max_len = max(len1, len2)
            
            # If we found a longer palindrome, update start and end
            if max_len > (end - start + 1):
                # For odd and even lengths, these formulas correctly compute the bounds
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        
        # Return the longest palindromic substring
        return s[start:end + 1]
