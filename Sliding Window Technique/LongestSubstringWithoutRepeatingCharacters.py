"""
    LeetCode #3 - Longest Substring Without Repeating Characters
    https://leetcode.com/problems/longest-substring-without-repeating-characters/
    
    Time Complexity - O(N)
    Space Complexity - O(1)
    Sliding Window & 2 Pointer Technique & Hashset
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        fast, slow = 0, 0
        max_cnt = 0
        hash_set = set()
        
        while fast < len(s):
            if s[fast] not in hash_set:
                # add the element in the set till it is repeated
                hash_set.add(s[fast])
                fast += 1
                max_cnt = max(len(hash_set), max_cnt)
            else:
                # remove the elements from set till the non repeating character
                hash_set.remove(s[slow])
                slow += 1
            
        return max_cnt
