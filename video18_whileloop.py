###  Python while Loop  ###
'''As the name suggests, while loops execute statements while the condition is True.
As soon as the condition becomes False, the interpreter comes out of the while loop.'''


# i = 0 
# while(i<3): # in this program we know that i value is 0 less than 3 so it run in the below we have added
#     print(i)
#     i = i + 1 # o+1= 1 , 1+1=2 , 2+2=4 -  it will not execute 
# print("Done with the loop!!")
#     #in each iteration we are increasing the value , and it will check the condition 

# g = (int(input("Enter the number : ")))
# while(g <= 40):
#     g = int(input("Enter the number : "))
#     print(g)
# print(" Done with the loop ")

####### Reverse while loop ###### Decrementing while loop 
# count = 10
# while(count >= 0):
#     print(count)
#     count = count -1 


# count = 5
# while(count > 0):
#     print(count)
#     count = count +1


'''Else with While Loop
We can even use the else statement with the while loop. 
Essentially what the else statement does is that as soon as the while loop condition becomes False, 
the interpreter comes out of the while loop and the else statement is executed.'''

# x = 5
# while(x > 0):
#     print(x)
#     x = x - 1
# else:
#     print('counter is 0')
    
    
'''Do-While loop in python
do..while is a loop in which a set of instructions will execute at least once (irrespective of the condition) 
and then the repetition of loop's body will depend on the condition passed at the end of the while loop.
It is also known as an exit-controlled loop.'''

'''How to emulate do while loop in python?
To create a do while loop in Python, you need to modify the while loop a bit in order to get similar behavior to a do while loop.

The most common technique to emulate a do-while loop in Python is to use an infinite while loop
with a break statement wrapped in an if statement that checks a given condition
and breaks the iteration if that condition becomes true:'''

while True:
    number = int(input("Enter the positive number : "))
    print(number)
    if not number > 0:
        break