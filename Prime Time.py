def PrimeTime(num):
  if num == 2:
    return True
  elif num % 2 == 0:
    return False
  else:
    return True
    
# keep this function call here  
print PrimeTime(raw_input())