#Questions
'''
Products of Array Except Self
Solved 
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O
(
n
)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
'''

#Solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if nums == [0]*len(nums):
            return nums
        product=1
        zero_exsist=False
        if 0 in nums:
            zero_exsist=True
            for i in nums:
                if i==0:
                    continue
                product=product*i
        else:
            for i in nums:

                if i==0:
                    continue
                product=product*i

        output_list=[0]*len(nums)
        for i in range(0,len(nums)):
            if zero_exsist and nums[i]==0:
                new_list = nums.copy()
                new_list[i] = 1
                print(new_list)
                if 0 in new_list:
                    output_list[i]=0
                    continue
                output_list[i]=product
            elif zero_exsist and nums[i]!=0:
                output_list[i]=0
            else:
                output_list[i]=int(product/nums[i])
        
        
        return output_list

        