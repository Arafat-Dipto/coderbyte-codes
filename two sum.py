def TwoSum(arr): 
  target=arr.pop(0)
  arr1=[]
  for i in arr:
      arr1.append(i)
      
  li2=[]
  c1=0
  c2=0
  for i in arr1:
      
      arr2= arr
      arr2.pop(c1)
      for j in arr2:
          
          c= i+j
          if c == target:
              #if not i in li2:
              li2.append(i)
              #if not j in li2:
              li2.append(j)
          
  ar = ""
  counter= 0
  for i in li2:
      counter=counter+1
      ar=ar+str(i)
      if counter%2 == 0:
          ar=ar+" "
      else:
          ar = ar+","
  if len(ar) == 0:
      ar = -1
  return ar

    
# keep this function call here  
print TwoSum(raw_input())