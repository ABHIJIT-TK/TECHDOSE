    def singleNumber(self, nums):
      return (sum(list(set(nums))*3)-sum(nums))//2
