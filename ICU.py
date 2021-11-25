
l = [1,2,3,3,2,1,2,5,6,4,5,6,7,6,7,8,6,5,4,3,5,6,7,8,8,1,2,3,4,5]

def customSort(l):
    finalL = []
    d = {}
    for item in l:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    lowest = l[0]
    for item in l:
        if item < lowest:
            lowest = item
            
    highest = l[0]
    for item in l:
        if item > highest:
            highest = item
            
    while lowest <= highest:
        if lowest in d:
            finalL += [lowest] * d[lowest]
        lowest += 1
        
    return finalL

print(customSort(l))
    
    