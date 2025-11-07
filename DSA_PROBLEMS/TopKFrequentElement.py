#Question
'''
 Top K Frequent Elements
Solved 
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
'''

#Solutions

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_dict={}
        for i in nums:
            print(i)
            if i in frequency_dict.keys():
                frequency_dict[i]+=1
            else:
                frequency_dict[i]=1
        output_list=[0]*k
        count_list=list(frequency_dict.values())
        for j in range(0,k):
            maximum_value=max(count_list)
            index=count_list.index(maximum_value)
            count_list[index]=0
            output_list[j]=int(list(frequency_dict.keys())[index])
        return output_list

            





        