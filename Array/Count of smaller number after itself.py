from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        a=SortedList()
        op=[]
        for i in nums[::-1]:
            b=SortedList.bisect_left(a,i)
            op.append(b)
            a.add(i)
        return reversed(op)
