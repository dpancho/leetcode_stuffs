class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ##if array is empty, return 0
        if not nums:
            return 0
        ##if not empty, initialize length to 1
        length = 1
        ##pointer
        i = 0
        ##iterate over array starting at j=1
        for j in range(1, len(nums)):
            ##if value at j != value at i, increment i+1 then swap values at indexes
            if nums[j] != nums[i]:
                i += 1
                nums[j], nums[i] = nums[i], nums[j]
                length += 1
        return length