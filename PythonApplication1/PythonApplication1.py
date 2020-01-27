def factorial(n):
    try :
     num= int(n)
     fact = 1
     if(num == 0 or num == 1):
      fact = 1
     else:
      for i in range (1,num+1):
        fact = fact*i
     return fact
    except ValueError:
        print("invalid input")
  

print("enter the number")
number = input()
print(factorial(int(number)))


    


    

