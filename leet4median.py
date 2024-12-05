class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_data = sorted(nums1+nums2)

        n = len(sorted_data) 
        mid = n // 2 
        
        if n % 2 == 0:
             median = (sorted_data[mid - 1] + sorted_data[mid]) / 2 
        else: 
            median = sorted_data[mid]
        return median

