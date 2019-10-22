def AlphabetSearching(str): 
  alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  for i in str:
      if i in alpha:
          alpha.remove(i)

  if len(alpha) == 0:
      return "true" 
  else: 
      return "false"

    
# keep this function call here  
print AlphabetSearching(raw_input())