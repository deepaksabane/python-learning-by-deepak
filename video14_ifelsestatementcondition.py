######## ifelsestatements #########
'''sometimes the programmer need to check the evaluation of certain expression (s) whether the expression
evaluate to true or false . if the expression evaluates to false , then the program evalution follows 
a diffrent path than it would have if the expression had evaluated to true '''

''' based on this conditional statements are further classified into following steps '''
# following types #
# if 
# if-else 
# if-else-elif 
# nested if-else-elif 

####  Conditional operators #####
# > greater than
# < less than 
# >= greater than or equal to 
# <=  less than or equal to 
# ==  equal to ( it will check the two numbers are qual or not )
# !=  not equal to 
c = int(input("Enter your Age : ")) # i have entered the value 18 in input 
print(c>18)  # false - it is not greater than 18 
print(c>=18) # true - it is not greater than 18 but it is equal to 18 
print(c<=18) # true - it is less than 18 or if it is equal to also it is fine 
print(c==18) # true - it is equal to 18 
print(c!=18) # false - because it is showing not equal to , but it is equal to 18 
if(c>18):
  print(" you can drive ") 
else:
  print( " learn driving first ")



# suppose we want to take the input bydefault it will take string as an input if we want integer than
a = int(input("Enter your Age : "))
b = (input("enter your name : "))
print("your age is : " , a , "\n"  "your  name is : ", b)

if(a>18):
  print(" you can drive ") 
else:
  print( " learn driving first ")


appleprice = 210
mybudget = 200
if(appleprice <=  mybudget):
    print("Add the apples to the cart and bring the apples to home.")
else:
    print("Through the apples to the shopkeeper ")



mangoprice = 10
budget = 50
if ( budget - mangoprice > 90):
    print("bring the apple to home")
elif (budget - mangoprice< 35):
    print(" tell shookeeper to keep there mango in his house ")
else:
    print("without eating mangoes we can survive")


### ifelse statement 
'''here in this it will check the condition if the condition matches then it will execute or else 
it will see the elif statement  , we can put n number of elif condition if the condition matches
it will execute '''

num = int(input("Enter the value of num : "))
if(num < 0):
    print(" The number is negative")
elif(num == 0 ):
    print(" Number is zero ")
elif(num == 999):
    print("Number is special")
else:
    print("Number is positve ")
    
print("Iam Happy now ")



####### Nested if statement #######
# if ke andar if laga diye aur yeh hum hazaar baar kar sakte hain 
num = 30
if(num < 0):
    print( " The number is negative ")
elif(num > 0 ):
    if(num <= 10 ):
     print( " The number is between 1-10 ")
    elif(num > 10 and num <= 20  ):
     print("The number is between 11 - 20 " )
    if(num >= 20 ):
      print(" The number is greater than 20")
else:
    print( " The number is zero")
    