# strings methods 
# python provides a set of build in methods that we can use to alter and modify the strings 



a = "deepak"
print(len(a))

# upper case & lower case  #
# The upper()methods converts a string to upper case 
# the lower() methods converts a string to lower case 
# strings are immutable means we cant change 
# it will not change the existing string we can create a new string by using string method 
print(a.upper())  # output will be DEEPAK
print(a.lower())  # output will be deepak


# rstrip #
# the rstrip() removes any trailing characters example 
# suppose the below example 
c = "shivansh!!!!!!!!!!"
print(c.upper())  # it will give the output as it is SHIVANSH!!!!!!!!!!

# but we want to get rstrip , it will remove the trailing character 
print(c.rstrip("!"))  # the output will be shivansh

# does it strip to leading escalation markks the answer is NO
d = "!!!shivanji!!!"
print(d.rstrip("!"))   # the output will be !!!shivanji


#########  replace() ###########
# the replace () method replaces all occurences of a string with another string 

e = "devops" 
print(e.replace("devops", "cloud"))  # The output will cloud 


########  split() #############

# The split() method splits the given string at the specified instance and returns the separated strings as list items

print(e.split())  # The output will be ['devops']

f = "devops !!!!! engineer"
print(f.split("  "))   # The output will be ['devops !!!!! engineer']

########### capitalize method #########

# The capatalize() methods turns only the first character of a string to upper case 
# and rest the other character of the strings to lower case . The string has no effect 
# if the first character is already uppercase 

blogheading = "introduction tO Python" # it will correct the other capital letter also 
print(blogheading.capitalize())  # Introduction to python


############ center() method ###########
# The center() methods aligns the string to the center as per the parameters given by the user 

deepak = " Welcome to Bhawani nivas "   
print(deepak.center(50))  # The out put will be  Welcome to Bhawani nivas
# here the letters will come in the middle how much value we will give it will give that much space
print(len(deepak))  #  lenth of string is 26 ok
print(len(deepak.capitalize())) # it added 26 spaces to comes at the center 


############## count() ###############
# The count() method returns the number of times the given value  has occured with the given string 

g = "deepak deepak sabane "
print(g.count("deepak"))  # The output will be 2 
# it will show how many times the word "deepak" is coming in a string 


############## endswith() ##############
# The endwith() method check if the strings ends with a given value .If yes then return true ,else return false 

h = "bahubali samrajayam !!!"
print(h.endswith("!!!"))  # The output will be true 
print(h.endswith("@@@"))  # The output will be false 

# we can also check the value in-between the srting by providing the start and end index position 

############ find() method ##############
# The find() method searches for the first occurence of the given value and returns 
# the index where it is present . if the given value is absent from the string then return -1

str2 = "my name deepak , he is the good  baby boy "
print(str2.find("baby")) # it will show the output 33 # it will show first occurence
print(str2.find("arati"))  # if it is not find the value it will return -1
print(str2.find("d")) # it will return the value 8 


############### index() #############
''' index() method searches for the firdst occurence of the given value and return the index
where it is present , if the given value is absent from the string then raise an exception '''
# count and index are same but in index it will show the exception 

str3 = " shivansh is good boy "
# print(str3.index("excellent")) # The output will be ValueError: substring not found
print(str3.index("boy"))

############### isalnum ################

'''The isalnum() method returns true only if the entire  string only consits of 
A-Z , a-z , 0-9 . If any other characters or punctuations are present , then it return false '''

str4 = "Wecolcome to the console"
print(str4.isalnum())   # the output will be false because it includes the spaces 

str5 = "Welcomtotheconsole"
print(str5.isalnum())  # the output will be true 


########### isalpha() #################

'''The isalpha() method returns true only if the entire  string only consits of 
A-Z , a-z  , if any other character or punctuation or numbers (0-9) are present, then it returns false '''

str6 = "welcome"
print(str6.isalpha())  # The output will be true 

str7 = "welcome009"
print(str7.isalpha()) # The outpur will be false 


############# islower() ###############
'''The islower() method returns true if all the characters in the string are lower case , else it returns false '''
str8 = "Heloo world"
print(str8.islower())  # it will return the value false it consists of uppercase 
str9 = "hello world"
print(str9.islower()) # it will return true it doesnt have capital letter 


############# isprintable() ################
'''The isprintable() method returns true if all the values within the given string are printable ,
if not , then return false '''

st1 = " we wish you happy dasera @ "
print(st1.isprintable())  # The output will be true 

st2 = " we wish you happy dasera \n"
print(st2.isprintable())  # it will show false because \n is not printable it will not be visible


################ isspace() #################
'''The ispace() method return true only and only if the strings contains white spaces, else return false'''

