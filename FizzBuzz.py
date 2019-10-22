def FizzBuzz(num):
  for n in range(1,num+1):
    string = " "
    if n % 3 == 0:
      string = string + "Fizz"
      
    if n % 5 == 0:
      string = string + "Buzz"
      
    if n % 5 != 0 and n % 3 != 0:
      string = string + str(n)
    print (string)
    
# keep this function call here  
FizzBuzz(raw_input())