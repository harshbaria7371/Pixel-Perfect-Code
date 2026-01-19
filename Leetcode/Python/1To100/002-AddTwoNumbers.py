# Description :

# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1

        val1, val2 = [l1.val], [l2.val]
        while l1.next:
            val1.append(l1.next.val)
            l1 = l1.next
        while l2.next:
            val2.append(l2.next.val)
            l2 = l2.next

        num1 = ''.join([str(i) for i in val1[::-1]])
        num2 = ''.join([str(i) for i in val2[::-1]])

        tmp = str(int(num1) + int(num2))[::-1]
        res = ListNode(int(tmp[0]))
        run_res = res

        for i in range(1, len(tmp)):
            run_res.next = ListNode(int(tmp[i]))
            run_res = run_res.next
        return res

    # Method 2:
    def addTwoNumbers_2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        if l1.val + l2.val < 10:
            l3 = ListNode(l1.val + l2.val)
            l3.next = self.addTwoNumbers_2(l1.next, l2.next)

        else:
            l3 = ListNode(l1.val + l2.val - 10)
            tmp = ListNode(1)
            tmp.next = None
            l3.next = self.addTwoNumbers_2(l1.next, self.addTwoNumbers_2(l2.next, tmp))
        return l3

        

# ============================================================================
# SOLUTION EXPLANATION
# ============================================================================
# 
# PROBLEM OVERVIEW:
# We have two linked lists where each node contains a single digit. The digits
# are stored in REVERSE order (least significant digit first). We need to add
# these two numbers and return the result as a linked list (also in reverse order).
#
# EXAMPLE:
#   l1: 2 -> 4 -> 3  (represents the number 342)
#   l2: 5 -> 6 -> 4  (represents the number 465)
#   Result: 7 -> 0 -> 8  (represents 807, which is 342 + 465)
#
# ALGORITHM APPROACH:
# This solution uses a "convert to integer" approach:
#   1. Extract all digits from both linked lists
#   2. Reverse the digit arrays to get the actual numbers
#   3. Convert to integers and add them
#   4. Convert the sum back to a string, reverse it, and build a new linked list
#
# STEP-BY-STEP BREAKDOWN:
#
# STEP 1: Edge Case Handling (lines 17-20)
#   - If l1 is empty, return l2 (adding 0 to a number)
#   - If l2 is empty, return l1 (adding 0 to a number)
#
# STEP 2: Extract Digits from Linked Lists (lines 22-28)
#   - Initialize val1 and val2 arrays with the first node's value
#   - Traverse each linked list using while loops
#   - Collect all digits into arrays: val1 = [2,4,3], val2 = [5,6,4]
#
# STEP 3: Reconstruct the Original Numbers (lines 30-31)
#   - Reverse the arrays: val1[::-1] = [3,4,2], val2[::-1] = [4,6,5]
#   - Convert each digit to string and join: "342", "465"
#   - These strings represent the actual numbers
#
# STEP 4: Perform Addition (line 33)
#   - Convert strings to integers: int("342") + int("465") = 807
#   - Convert sum back to string: "807"
#   - Reverse the string: "708" (because result must be in reverse order)
#   - Note: tmp is now a string of digits in reverse order
#
# STEP 5: Build Result Linked List (lines 34-39)
#   - Create first node with first digit converted to integer: ListNode(int(tmp[0]))
#     Note: tmp[0] is a string character, so we convert it to int (e.g., "7" -> 7)
#   - Use a runner pointer (run_res) to traverse and build the list
#   - For each remaining digit, convert to int and create a new node: ListNode(int(tmp[i]))
#   - Link each new node to the previous one
#   - Result: 7 -> 0 -> 8 (all nodes contain integer values, not strings)
#
# NOTE: This solution works well for small to medium numbers, but for very large
# numbers (beyond Python's int range), a digit-by-digit addition approach would
# be more appropriate to avoid potential overflow.
# ============================================================================

# ============================================================================
# METHOD 2 EXPLANATION (Recursive Approach)
# ============================================================================
# 
# ALGORITHM APPROACH:
# Method 2 uses a RECURSIVE approach that processes digits one at a time,
# handling carry propagation naturally through recursive calls. This method
# works directly with the linked list structure without converting to integers.
#
# KEY ADVANTAGES:
# - No integer conversion needed (works with arbitrarily large numbers)
# - More memory efficient (processes nodes as it goes)
# - Handles carry propagation naturally through recursion
#
# STEP-BY-STEP BREAKDOWN:
#
# STEP 1: Edge Case Handling (lines 44-47)
#   - If l1 is empty, return l2 (adding 0 to a number)
#   - If l2 is empty, return l1 (adding 0 to a number)
#   - This handles lists of different lengths
#
# STEP 2: Check if Sum Needs Carry (line 49)
#   - Calculate sum of current digits: l1.val + l2.val
#   - If sum < 10: No carry needed, proceed normally
#   - If sum >= 10: Need to propagate carry to next position
#
# STEP 3A: No Carry Case (lines 50-51)
#   - Create new node with the sum: ListNode(l1.val + l2.val)
#   - Recursively process next nodes: addTwoNumbers_2(l1.next, l2.next)
#   - Link the result to current node's next pointer
#   - Example: 3 + 4 = 7, create node(7), then process next digits
#
# STEP 3B: Carry Case (lines 54-57)
#   - Create new node with (sum - 10): ListNode(l1.val + l2.val - 10)
#     This gives us the ones digit (e.g., 7 + 8 = 15, store 5)
#   - Create a carry node: ListNode(1) representing the carry
#   - Recursively add the carry to the next position:
#     First, add l2.next with carry: addTwoNumbers_2(l2.next, tmp)
#     Then, add l1.next with that result: addTwoNumbers_2(l1.next, ...)
#   - Link the result to current node's next pointer
#
# EXAMPLE WALKTHROUGH:
#   l1: 2 -> 4 -> 3  (represents 342)
#   l2: 5 -> 6 -> 4  (represents 465)
#
#   Call 1: addTwoNumbers_2([2,4,3], [5,6,4])
#     - 2 + 5 = 7 < 10, no carry
#     - Create node(7)
#     - Recursively call: addTwoNumbers_2([4,3], [6,4])
#
#   Call 2: addTwoNumbers_2([4,3], [6,4])
#     - 4 + 6 = 10 >= 10, need carry
#     - Create node(0) (10 - 10 = 0)
#     - Create carry node(1)
#     - Recursively: addTwoNumbers_2([3], addTwoNumbers_2([4], [1]))
#
#   Call 3: addTwoNumbers_2([4], [1])
#     - 4 + 1 = 5 < 10, no carry
#     - Create node(5)
#     - Recursively: addTwoNumbers_2(None, None) -> returns None
#
#   Call 4: addTwoNumbers_2([3], [5])
#     - 3 + 5 = 8 < 10, no carry
#     - Create node(8)
#     - Recursively: addTwoNumbers_2(None, None) -> returns None
#
#   Result: 7 -> 0 -> 8  (represents 807)
#
# RECURSION FLOW:
# The recursion naturally handles:
# - Lists of different lengths (edge cases return the non-empty list)
# - Carry propagation (carry is added as a new node in recursive call)
# - Building the result list (each recursive call returns a node, linked together)
#
# COMPLEXITY ANALYSIS:
# - Time Complexity: O(max(m, n)) where m and n are lengths of l1 and l2
# - Space Complexity: O(max(m, n)) due to recursion stack
#
# NOTE: This recursive approach is elegant but has a potential issue - when
# lists have different lengths and one becomes None, the recursive call with
# None might need additional handling. The edge cases at the start help, but
# the carry propagation logic could be improved for robustness.
# ============================================================================