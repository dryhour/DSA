import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        median = 0

        nums = sorted(nums1 + nums2)

        length = len(nums)
        if length % 2 == 0:
            middle = int(length/2)
            median = (nums[middle-1]+nums[middle])/2
        else:
            median = nums[int(math.ceil(length/2))-1]

        return median
