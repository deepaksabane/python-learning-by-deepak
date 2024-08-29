### Match Case Statements ###
'''A match statement will compare a given variable’s value to different shapes, 
also referred to as the pattern. The main idea is to keep on comparing the variable with all the present 
patterns until it fits into one.

The match case consists of three main entities :

The match keyword One or more case clauses Expression for each case
The case clause consists of a pattern to be matched to the variable, a condition to be evaluated
if the pattern matches, and a set of statements to be 
executed if the pattern matches.'''

# here we need to match the cases for example 
x = int(input("Enter the value of the x : "))
# x is the variable to match 
match x:
    # if x is 0 
    case 0:
        print(" case is zero")
    case 1:
        print(" case is one")
    case 39:
        print(" case is thirty nine ")
    case _:
        print(x)  # whatever the input we will give it will show that if above case will not match 