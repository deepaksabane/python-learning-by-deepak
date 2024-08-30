###  Python while Loop  ###
'''As the name suggests, while loops execute statements while the condition is True.
As soon as the condition becomes False, the interpreter comes out of the while loop.'''


i = 0 
while(i<3): # in this program we know that i value is 0 less than 3 so it run in the below we have added
    print(i)
    i = i + 1 # o+1= 1 , 1+1=2 , 2+2=4 -  it will not execute 
print("Done with the loop!!")
    #in each iteration we are increasing the value , and it will check the condition 

g = (int(input("Enter the number : ")))
while(g <= 40):
    g = int(input("Enter the number : "))
    print(g)
print(" Done with the loop ")

####### Reverse while loop ###### Decrementing while loop 
count = 10
while(count >= 0):
    print(count)
    count = count -1 



    