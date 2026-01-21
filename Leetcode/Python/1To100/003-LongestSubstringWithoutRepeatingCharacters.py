# Description :
# Given a string s, find the length of the longest substring without duplicate characters.
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.

class Solution:
    def longestSubstringWithoutRepeatingCharacters(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        right = 0
        max_length = 0
        while right < len(s):
            if s[right] in s[left:right]:
                left += 1
            else:
                right += 1
            max_length = max(max_length, right - left)
        return max_length

# ============================================================================
# SOLUTION EXPLANATION
# ============================================================================
# 
# PROBLEM OVERVIEW:
# We need to find the length of the longest substring that contains no
# repeating characters. A substring is a contiguous sequence of characters
# within the string.
#
# EXAMPLE:
#   Input: "abcabcbb"
#   Output: 3
#   Explanation: The longest substring without repeating characters is "abc"
#
# ALGORITHM APPROACH:
# This solution uses a SLIDING WINDOW technique with two pointers:
# - left pointer: marks the start of the current window
# - right pointer: marks the end of the current window (exclusive)
# The window s[left:right] always contains unique characters.
#
# STEP-BY-STEP BREAKDOWN:
#
# STEP 1: Edge Case Handling (lines 18-19)
#   - If the string is empty, return 0 (no substring exists)
#
# STEP 2: Initialize Pointers and Variables (lines 20-22)
#   - left = 0: Start of the sliding window
#   - right = 0: End of the sliding window (exclusive, so window is s[left:right])
#   - max_length = 0: Tracks the maximum length found so far
#
# STEP 3: Sliding Window Algorithm (lines 23-28)
#   The algorithm expands and contracts the window:
#
#   a) Check for Duplicate (line 24):
#      - Check if s[right] (current character) already exists in s[left:right]
#      - This substring check ensures the current window has no duplicates
#
#   b) If Duplicate Found (line 25):
#      - Move left pointer one position to the right
#      - This contracts the window from the left, removing the duplicate
#      - Note: The right pointer stays the same, so we re-check the same character
#
#   c) If No Duplicate (line 27):
#      - Move right pointer one position to the right
#      - This expands the window to include the new character
#
#   d) Update Maximum Length (line 28):
#      - After each iteration, calculate current window length: (right - left)
#      - Update max_length if current window is longer
#
# EXAMPLE WALKTHROUGH:
#   Input: s = "abcabcbb"
#
#   Iteration 1: left=0, right=0, window=""
#     - s[0]='a' not in "", expand: right=1, window="a"
#     - max_length = max(0, 1-0) = 1
#
#   Iteration 2: left=0, right=1, window="a"
#     - s[1]='b' not in "a", expand: right=2, window="ab"
#     - max_length = max(1, 2-0) = 2
#
#   Iteration 3: left=0, right=2, window="ab"
#     - s[2]='c' not in "ab", expand: right=3, window="abc"
#     - max_length = max(2, 3-0) = 3
#
#   Iteration 4: left=0, right=3, window="abc"
#     - s[3]='a' in "abc", contract: left=1, window="bca" (right stays 3)
#     - max_length = max(3, 3-1) = 3
#
#   Iteration 5: left=1, right=3, window="bca"
#     - s[3]='a' not in "bca" (wait, we already checked this...)
#     - Actually, s[3]='a' is at index 3, and window is s[1:3]="bc"
#     - s[3]='a' not in "bc", expand: right=4, window="bca"
#     - max_length = max(3, 4-1) = 3
#
#   Continue until right reaches end of string...
#   Final result: max_length = 3
#
# KEY INSIGHTS:
# - The window s[left:right] always maintains the invariant of having unique characters
# - When a duplicate is found, we shrink from the left until the duplicate is removed
# - The algorithm ensures we check all possible substrings without missing any
#
# COMPLEXITY ANALYSIS:
# - Time Complexity: O(n²) in worst case
#   - The substring check `s[right] in s[left:right]` is O(n)
#   - In worst case (all characters same), we do this for each character: O(n²)
#   - Can be optimized to O(n) using a hash set to track characters
#
# - Space Complexity: O(1)
#   - Only uses a constant amount of extra space for variables
#   - The substring slicing creates temporary strings, but they're not stored
#
# OPTIMIZATION NOTE:
# A more efficient O(n) solution would use a hash set (or dictionary) to track
# characters and their last seen positions, allowing us to jump the left pointer
# directly to the position after the duplicate character instead of moving it
# one step at a time.
# ============================================================================