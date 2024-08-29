'''Introduction to Loops
Sometimes a programmer wants to execute a group of statements a certain number of times
This can be done using loops. Based on this loops are further classified into following main types;
for loop
while loop
The for Loop
for loops can iterate over a sequence of iterable objects in python. 
Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.'''


name = "abhishek"
for i in name:
    print(i)  # for string 


iterating over a list 
colors = ["Red", "orange" , "purple", "jamun"]
for color in colors:
  print(color)  # we are taking the value in colors 
  for i in color:  #  here we considering the value of color  # s is not there in color
     print(i)


'''range():
What if we do not want to iterate over a sequence? 
What if we want to use for loop for a specific number of times?
Here, we can use the range() function.'''

for d in range(10):
 print(d)  # The output will be 0-9 Here, we can see that the loop starts from 0 by 
          # default and increments at each iteration.But we can also loop over a specific range.
# if you want to print the value from from 1 then '
 print(d + 1)
 
for g in range(2 , 15):
    print(g)
 
for k in range(1, 12 , 4):
  print(k) # The loop starts at 1 and increments by 4
  #in each iteration until it reaches a value that is less than 12. 