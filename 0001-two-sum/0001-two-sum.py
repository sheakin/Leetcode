class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        previousmap = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in previousmap:
                return [i,previousmap[dif]]
            previousmap[nums[i]] = i