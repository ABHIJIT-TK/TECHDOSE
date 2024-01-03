 def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num3=[]
        nums1.extend(nums2)
        num3.extend(nums1)
        num3.sort()
        l=len(num3)
        if l%2==1:
            return num3[l//2]
        else:
            return (num3[l//2]+num3[l//2-1])/2

