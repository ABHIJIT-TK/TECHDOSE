    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m={}
        for i,j in enumerate(nums):
            d=target-j
            if d in m:
                return [m[d],i]
            m[j]=i
        return 
        
