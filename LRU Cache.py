def LRUCache(strArr):
    cList = []
    for i in strArr:
        if i in cList:
            cList.remove(i)
            cList.append(i)
        else:
            if len(cList) > 4:
                del cList[0]
            cList.append(i)
            
    result = ""
    for n in cList:
        result=result+n+"-"
    result= result[:-1]
    return result

# keep this function call here  
print LRUCache(raw_input())