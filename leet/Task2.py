def insert(intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    if (len(intervals) == 0):
        return [newInterval]
    result = []

    changed = False
    for i in range(0,len(intervals)):
        if (changed == True): 
            break
        
        #checking where first newInterval value should be placed
        if (newInterval[0] < intervals[i][0]):
            for j in range(i, len(intervals)):
                if (newInterval[1] < intervals[j][0]): #both values smaller then currently check interval
                    result.append([newInterval[0], newInterval[1]])
                    changed = True
                    break
                
                elif (newInterval[1] >= intervals[j][0] and newInterval[1] <= intervals[j][1]): #second value is in the interval
                    result.append([newInterval[0],intervals[j][1]])
                    changed = True
                    break
                elif (newInterval[1] > intervals[j][1] and len(intervals) == j + 1):
                    result.append([newInterval[0],newInterval[1]])
                    changed = True
                    break
        elif (newInterval[0] >= intervals[i][0] and newInterval[0] <= intervals[i][1]):
            for j in range(i, len(intervals)):
                if (newInterval[1] < intervals[j][0]): #both values smaller then currently check interval
                    result.append([intervals[i][0], newInterval[1]])
                    changed = True
                    break
                
                elif (newInterval[1] >= intervals[j][0] and newInterval[1] <= intervals[j][1]): #second value is in the interval
                    result.append([intervals[i][0],intervals[j][1]])
                    changed = True
                    break
                elif (newInterval[1] > intervals[j][1] and len(intervals) == j + 1):
                    result.append([intervals[i][0],newInterval[1]])
                    changed = True
                    break
    
        elif (changed == False):
            result.append(intervals[i])
        else:
            break
    for interval in intervals:
        if interval[0] > result[-1][1]:
            result.append(interval)
    
    if (result[-1][1] < newInterval[0] and changed == False):
        result.append(newInterval)
    return result
                
            
        
            
        
                
intervals = [[2,4]]
newInterval = [2,5]
print(insert(intervals, newInterval))
