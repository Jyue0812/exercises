class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i ==0:
                a = nums.pop(nums.index(i))
                nums.append(a)
        return nums


nums = [0, 1,1,0, 2]
s = Solution()
print(s.moveZeroes(nums))