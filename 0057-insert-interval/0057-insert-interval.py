class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        insert=False
        res=[]
        for i in range(len(intervals)):
            start=intervals[i][0]
            if insert==False and start>newInterval[0]:
                res.append(newInterval)
                insert=True
            res.append(intervals[i])
        if insert==False:
            res.append(newInterval)
        intervals=res
        start1=intervals[0][0]
        end1=intervals[0][1]
        res=[]
        for i in range(1,len(intervals)):
            start2=intervals[i][0]
            end2=intervals[i][1]
            if end1>=start2:
                end1=max(end1,end2)
                continue
            res.append([start1,end1])
            start1=start2
            end1=end2
        res.append([start1,end1])
        return res