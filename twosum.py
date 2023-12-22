"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


"""
#  O(n^2) brute force 
import math 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
                    find=target- nums[i]
                    for j, el in enumerate(nums[i+1:]):
                        if find == el:
                            ans = [i,j+1+i]
                            print(ans)
                            return ans

# O(N) hashmap
import math 
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums={}
        for i in range(len(nums)):
            dict_nums[nums[i]]=i  
        for i in range(len(nums)):
                    find=target- nums[i]
                    if find in dict_nums and  dict_nums[find]!=i :
                        ans = [i,dict_nums[find]]