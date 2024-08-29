# To Take the user input we will use input function 
# In python we can take the user input directely using the input() function , This
# input function gives a return value as string/character hence we have to pass that into a variable

# suppose we have a=input() and do print(a) then we need to enter any value deepak
# a= input()
# print(a) # it will ask for the input 


# we can give a string into it 
a = input( "Enter your name : ")
print("My name is ", a)


x= input("Enter first number: ")
y= input("Enter second number: ")

print(x + y ) # it will show whatever you put in value not addition why?

###########Rule##############
# here in x whatever you put the value it will consider as a string input function is nt intelligent 
# so the solution is we need to put the type in it 

print(int(x) + int(y))  # type we can define so that it can understand
