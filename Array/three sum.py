    def threeSum(self, nums: List[int]) -> List[List[int]]:
        li=[]
        nums.sort()
        for i,j in enumerate(nums):
            if i>0 and j==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                s=j+nums[l]+nums[r]
                if s<0:
                    l+=1
                elif s>0:
                    r-=1
                else:
                    li.append([j,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1]and l<r:
                        l+=1
        return li
