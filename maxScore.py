""" STRING 
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).
The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

Runtime =33 ms
Beats 95.62% of users with Python3
"""
class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones=s.count("1")
        output=0
        if ones==0 or ones==len(s):
            return len(s)-1
        else: 
            zeros= len(s)-ones
        for i in range(len(s)-1): 
            temp_zeros = s[:i+1].count("0")
            temp_ones= ones- i-1 + temp_zeros
            temp=temp_zeros+temp_ones
            if output<temp:
                output=temp 
        return output
