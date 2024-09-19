# LC704: https://leetcode.com/problems/binary-search/description/
# Binary Search

'''
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''
# left and right close
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
# left clode and right open
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        # the intervdal is not valid if left == right
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        return -1     

# LC27: Remove Element: https://leetcode.com/problems/remove-element/description/
'''
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
The remaining elements of nums are not important as well as the size of nums.
Return k.
'''
# Two pointers
# fast pointer to iterate the array
# slow pointer to record the position of the element which is not equal to val
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return None
        fast, slow = 0, 0
        while fast in range(len(nums)) :
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow 

# LC977 Squares of a Sorted Array: https://leetcode.com/problems/squares-of-a-sorted-array/
'''
Given an integer array nums sorted in non-decreasing order, 
return an array of the squares of each number sorted in non-decreasing order.

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
'''

# Three pointers
# l, r, i, use i to record the position of the result
# compare the square of the left and right pointer

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r, i = 0, len(nums)-1, len(nums)-1
        res = [0] * len(nums)
        while l <= r:
            if nums[l] ** 2 < nums[r] ** 2:
                res[i] = nums[r] **2
                r -= 1
            elif nums[l] ** 2 >= nums[r] ** 2:
                res[i] = nums[l] **2
                l += 1
            i -= 1      
        return res






