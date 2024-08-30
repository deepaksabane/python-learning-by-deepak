'''break statement
The break statement enables a program to skip over a part of the code. 
A break statement terminates the very loop it lies within.'''

# jab bhi hum ek loop ko istemal karte hain , hum kabhi kabhi chahate hain yeh loop yahin khatam hokar 
# exit kar jaaye , aise me hum break statement kla istemal karte hain 



for i in range( 12 ):
    if(i == 10):
        break
    print("5 X ", i+1 , "=", (5 * (i+1) )) # this is the 5 table suppose we want to end this at 8 we can put condition 
    
print("Loop ko chord kar chale jaavo")
for z in range (20000):
    print("5 X " , z , "=" , 5 * z )



'''Continue Statement
The continue statement skips the rest of the loop statements and causes the next iteration to occur.'''

# kabhi kabhi hum kisi loop ke iteration ko skip karna chahate hain tab hum continue ka istemal karte hain

for i in range(12):
    if(i == 10):
        print("skip the iteration")  # here it will skip and again continue the iteration 
        continue
    print("5 X", i , "=", 5 * i)