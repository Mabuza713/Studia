def merge(intervals):
    intervals = sorted(intervals, key=lambda l:l[0])

    result = [intervals[0]]
    for interval in intervals[1:]:
        # building uppon result
        changed = False
        for i in range(0,len(result)):
            print(result)
            # Value contained by bracket
            if (result[i][0] <= interval[0] and result[i][1] >= interval[0]):
                if (result[i][1] >= interval[1]):                    
                    changed = True
                    break
                elif (result[i][1] < interval[1] and result[i][0] < interval[1]):
                    temp = result[i]
                    
                    result[i] = [temp[0], interval[1]]
                    changed = True
                    break

            elif (result[i][0] > interval[0] and result[i][1] >= interval[1]):
                if (result[i][0] <= interval[1]):
                    temp = result[i]
                    result[i] = [interval[0], temp[1]]
                    changed = True
                    
                    break

            elif (result[i][0] >= interval[0] and result[i][1] <= interval[1]):
                changed = True
                result[i] = [interval[0], interval[1]]
                break
            
        if (changed == False):
            result.append(interval)




    return result




intervals1 = [[2,3],[4,5],[6,7],[8,9],[1,10]]
#intervals2 = [[1,3],[2,6],[8,10],[15,18]]
#intervals3 = [[1,4],[4,5]]

print(merge(intervals1))
#print(merge(intervals2))
#print(merge(intervals3))