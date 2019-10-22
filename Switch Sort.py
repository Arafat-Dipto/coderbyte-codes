def SwitchSort(arr): 
  swap = 0
  visited =  [False for i in range(len(arr))]
  for i in range(len(arr)):
    j = i
    counter = 0
    while not visited[j]:
      visited[j] = True
      j = arr[j]-1
      counter= counter+1
    if counter!= 0:
      swap=swap+(counter-1)
  return swap

    
# keep this function call here  
print SwitchSort(raw_input())