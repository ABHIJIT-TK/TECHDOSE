    def merge(self, inter: List[List[int]]) -> List[List[int]]:
        inter.sort()
        a=[]
        for i in range(len(inter)):
            st,end=inter[i][0],inter[i][1]
            if a and end<=a[-1][1]:
                continue
            for j in range(i+1,len(inter)):
                if inter[j][0]<=end:
                    end=max(end,inter[j][1])
                else:
                    break
            a.append([st,end])
        return a
