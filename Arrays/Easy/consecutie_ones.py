# https://leetcode.com/problems/max-consecutive-ones/description/

# Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

# Example 1:

# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
# Example 2:

# Input: nums = [1,0,1,1,0,1]
# Output: 2

def findMaxConsecutiveOnes(nums):
        length = len(nums)
        result , potential= 0 , 0
        for i in range(length):
            if nums[i] == 1 :
                potential+=1
            elif nums[i]==0 and potential > result:
                result = potential
                potential = 0
            else :
                potential =0
        
        return max(result,potential)


nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))