##############Type Casting #####################
# type casting is the converstion of one datatype to other datatype is known as typecasting 
# python supports a variety of functions  or methods  like : int(), float(), str(), ord(), 
# hex(), set(), list(), dist(), tuple(),  for the typecasting in python 

# Two types of type casting 
# explicit converstion  - main kar raha hun chahakar 
# implicit converstion  - python automatically kar raha hai 



# let say suppose we have created a string and inside that we have added number and we add
# 3 then it will not come 30 because 27 is a string and 3 is integer
# so for this in double qoutes we have written its a digit to tell python 
# so we need to do typecast to an integer 
# suppose you will have value a = "1" and b = "2" then print(a+b) it will show 12 
# because python doesnt know the string as it is it will print 
a = "1"
b = "2"
c = 1
d = 2
e = "shivansh"
f = "sabane"
print(a+b) # it will print 12 
print(c+d) # it will print 3 
print(e+f) # shivanshsabane

# here how we can convert  ( explicit converstion) manually converstion  as per our requirement 
s = "12"
q = "12"
print(int(s) + int(q)) # it will show 24 
print(int(s+q)) # it will show 1212
# if you want to give  that s= 12harry and put int and try to add it will show error 

string = "15"
number = 7 

string_number = int(string) # here we are storing the value of string as an 15 
sum = number + string_number # doing addition here 
print(" The sum of both the number is : " , sum) # answer is 22 

###### implicit datatype ##########
# python converts a smaller datatype to a higher datatyoe to prevent data lose

w = 8.9
z = 9
print (type (w+z) )
# here we get the result in float , python does automatically here 
# The value of w remains in float and the value of z also float 
# float + float 
