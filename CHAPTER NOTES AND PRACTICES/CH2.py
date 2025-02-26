


# variables cannot start with numbers, contain spaces, use special characters, be a reserved word(if,or,else, while, for, def)
# { } braces are used to to direct an object when expressed with a function inside a string
# ( ) are used to call functions and pass agruments to them print(ex), 
#used to group expressions to control the order of operation number(2 + 3)*4 prints 14
#used to define tuples ex (blue,green, yellow) or (1,2,3)


from tkinter.tix import INTEGER


print()

pie = 3.14
whatever =f"I ate some{pie} and it was good"
print(whatever)

print(pie, "I ate some pie and it was good ")
print("I ate some",pie,"and it was good")
print("i ate some",pie + 1,"and it was good")

print()
fruit= "banana"
what = f"i love(fruit)"
print(what)
what2 = f"I love{fruit}"# {} curly braces are directing the object when expression a function
print(what2)

print()
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)#total_sum = 1 + 2 + 3 + 4 + 5 remember, its in brackets with commas separating each integer. 


print("the sum of the numbers is:" ,+ total_sum)#because we are not printing a Function, we do not need the braces. the + combines to string with the variable
print(f"the sum of the numbers is: {total_sum}")# bc total_sum is inside of a string AND WE ARE PRINTING A FUNCTION, we need the braces to separate it from the rest
#

print()

redbull = [99, 20,]

total = sum(redbull)

print("the sum of the Redbull:" ,+ total) 
print(f"the sum of the redbull {total}") # ^both print the same

print(f"why {total}")# why 199




print()
number = 7
string =f"{number+1} is just another number"
print(string)





print()
age = 49
years=10
string1="in {} years and i will be {}". format(years,age)
print(string1)    

string2 = "in %d years i will be %d" %(years,age)
print(string2)

string3 =f"in{years} i will be{age}"
print(string3)
#string1 and 2 are two older version of using f. below newer easier way,
#when using older way 1 is str.format()method and %formatting. with % must use %s for string and %d for integers



print()


#str.capitalize() returns a string with first letter capitalized and the rest lower

print("hello world".capitalize())#output Hello world
print("HELLO world".capitalize()) #output Hello W")

#str.lower() converts all letters into lower
print("WORLD, worLd" .lower()) #output world and world

#str.upper() converts all letters into uppercase
print("bitcoin is the bESt tHIng known".upper())# all letters uppercase

#str.startswith() checks whether a string starts with a specific prefix 
#output will be \ true or false(Boolean is data type that hold one of two values ( for.startwith the boolean repsonse is true or false )

text = "Bitcoin is the number 1 crypto asset"

print(text.startswith("Bitcoin")) #will produce true
print(text.startswith("bitcoin"))   #will produce fase since b is not capitalized
print(text.startswith("Bi"or"B")) # produces true bc both are true
print(text.startswith("bi"or"B")) # produces false bc first request is false
print(text.startswith("number 1")) #will produce false

print()#print() will create a break in the output

#str.endswith same thing

print(text.endswith("et")) #true
print(text.endswith("asset"))#true
print(text.endswith("t"))#true
print(text.endswith("ass"))#false bc it doesnt involve the last part of the word asset, only the begining
print(text.endswith("sset"))#true bc opposite of ass
print(text.endswith("se"))#false doesnt have the t in asset to complete it as a true statement

print()
#str.stip() method returns a copy of string with leading and trailer characters remove is case sensitive, if space is leading strip("") will remove space
print(text.strip("Bitcoin"))# removes Bitcoin from "text" variable
print(text.strip("1")) # will not rmove 1 bc its not leading
print(text.strip("B")) #will produce itcoin ''' removes the leading "B"
print(text.strip("Bit"))
print(text.strip("sset"))# will produce bitcoin is the 1 number a - bc sset is trailing

print()


#***be careful when writing programs and using formatting. it will pick up previous command formatt***

#str.replace takes 2 substring and replaces old one with new one. case senstive 

gold = "gold will be the best asset"

print(gold.replace("gold","bitcoin").replace("will","is"))# can combine similiar formatting commands
print(gold.strip("gold").strip("asset"))
print()
#print(gold.strip("gold").replace("best","worst") cannot combine 2 different commands
results = gold.strip("gold").replace("best","worst")# produces -  will be the worst asset
print(results)# way to combine 2 formatting create new expression with both command and print that

print()
#escape sequences- sequence of characters that do not represent the literal meaning when inside of a string
# escape characters tell complier to interpret the next character(s) in a special way and ingore as usual meaning
#this creating the escape \n

print("hi\nthere") # prints "hi" on one line and "there" next line
print("weekend at bernie\n"*3)
print()
mixlist = [1,2,3,4,5],"spring","summer", [6,7,8,9,10]#
print(len(mixlist))#4 - lens will tell you the number of values in expression. in this example  1-5 + 2 strings(words in this case) +[2 bracket]= 4 elements if the 2 words where in Parentheses  this would be 3 values
#if the all [ ]s where removed it would be 12. 
#since the value has commas and [] that separate 2 list group values, its consider a tuple. if it was all in [] it would be a list

#example of tuple, ('1','2','3') example of tuple containing list - =[1,2,3]"a","b"] 3 values
print()

mixlist2 = [1,2,3,4,5,"spring","summer", 6,7,8,9,10]#12- since the closing ][ were removed, this is consider a list making it a list containing 12 values
print(len(mixlist2))#12 
print()

numbers =[1,2,3,4,5,6]#list
print(len(numbers))#6

print()
\
#slicing

list1 = [10,11,12,13,14,15,16]

print(list1[1:5])# will print from [11,12,13,14] rememeber 0 is a place which is the 10 number .slicing produces
# the values within the slice this example 0-4

print(list1[1:])# well all values after the value in the 1 location 11-16

print(list1[:4])#will print all values from the 4th location to the 0th location 10,11,12,13

print()

#combining list
numbers =[1,2,3,4,5,6]
abc = ['a','b','c','d','e','f'] #side note, a-f would be consider a one value if not comma

print(numbers + abc)
 # combines the two list a-f,1-6
#print[numbers + abc] # trying to print with [] is like requesting the complier to "created" a list of numbers then print it
#you have to set the variable then print it

te = ('q''a''xc') #lens as 4 when w/o commas, 4 characters
te2 =('q','a','xc')# lens will be 3 bc commas separate into 3 values
te3= ['q''a''xc'] # lens will be 1, [] is like the literally 
te4=[ 'q','a','xc']# by adding commas, you telling complier within this list how many groups of letters =3
#print(len(te + te)) 8
#print(len(te + te2)) you cant len 2 arguments at a time have to create new expression combining the 2 values

print()

changelist = ["bitcoin","jimmy","lily"] # Only when making changes to a list with strings
changelist[2] = "xrp"

print(changelist)# lily is replace with Nikolai

print()

print(te.replace('q','b')) #when changing a non tuple variable of te.. has no commas AND qoutes separating values
#print(te2.replace('q','b')) tuples are immutables again a tuple is values inside parathanese with commas

# list are values inside of [] brackets and they mean literal.List are mmutable. [1234] is consider a list with 1 value when no commas
# verus [1,2,3,4] a list with 4 values with commas

print()

sentence = "this is a sentences of an explanation of a string"
print(sentence.replace("explanation","example"))
print(sentence)

print()

number2 = [1,2,3,4,5,6]
number2[1] = 'ON'# produces [1,ON,3,4,5,6] remember 0 is a spot. your asking the literal [1]spot
print(number2)

print()

number22 =[12]
number22[0]= "one"
print(number22)# produces [one]. the number22 variable is a list containing 1 value in the 0 spot 

print()


s = """bitcoin is all"""
print(s[-14],s[-13],s[-12],s[-11],"h",s[-14],s[-13],s[-12],"ches")



print()

# list appendix is a method to insert a value in the end
appendlist = ['a','b','c','d','e','f','g']

print()

appendlist.append("a") 
print(appendlist)# added an a after g in the list

print()

# you can slice through a list and replace the target with whatever other values
slicereplace =[0,1,2,3,4,5,6,7,8,9,]
slicereplace[0:5]=["a","b","c","d"]
print(slicereplace)

print()
#Boolean data types are values that can only be one of two values, True or False. 
#For example, the proposition 100 is more than 5 is True, and thus, it would have a True Boolean value. 
#On the other hand, the proposition The sky is green is False, and thus, it would have a False Boolean val



print(type(True)) # produces the class type Boolean
false = 'false'
print(type(false)) # produces the class tpye String bc lower case false is define as false
#False ='false'  #cannot be done bc uppercase False is a reserve word

#COMPARSION OPERATORS##
#comparison operations  are values of objects or the objects indentities theselve
#like less than <, greater >,
#<= less than or equal to, >= greater than or equal to,
#== equal to, != not equal to, is object identity




print()
print(10<1) #produces false

print()
print(len("open")<=4) #true 4 letters in open and the number 4 are equal 

print()
print(len("open")>=4)#true how many letters in open with len, and then the Equation 
# confusion on parathenes. you need two sets bc its two commands. 1 

print()
print(len(["bananananananananananana"])>2) #false a list with one value is less than the #2

print()
print("foobar" == "foobar")# true. only one set of parathenese
#bc all you are asking is if the two words are equal

print()
print("foobar" != "foobar") #false they equal

print()
l = [1,2,3]
l2 = l
print(l is l2)# true l is lowercase 1 idk(ask) but the statement is true because
#afer each python 284,285 you press enter. it stores the statement in the memory
# making the print job as true when using is function

print()

print(l is not None)# true. bc l points to something in 
#the memory therefore not null




print()
print()

#LOGICAL OPERATORS#

#not x - returns false if x is true,else false

# x and y- returns x if x is false, else returns y 

# and is a circuit operator and only evaulates 
# second argument if the first is True

# x or y - returns y if x is false, else returns x 

# or is a short operator in that it will only evaulate 
# the second agrument if the first is one is false

x = 10
y = 20
z = 30
print(x < y and y>z) # false- b/c and operators look at 2nd argument
# only if the 1st is true. since 10<20 is true, it looks at 20>30 which is false
print(x > y and y<z) #  false - the first agrument is false. no need 2nd
print(z > x and y > x)# true, 1st is true, 2nd is true. go w/ 2nd answer 


print()
a = 1
b = 2
c = 3
print(a > b or a < b)#true- 1 greater than 2 is false so we look at 2nd argument
# 1 is less 2 which is true. or operators only look at 2nd arg if first is false
print(c > a or b >a)# true - since first agr is true
print(a > c or b > a) # true looks at 2nd since 1st is false
print(a > c or a > c)# flase, 2st false 2nd is false two


print()
# OR operators return the answer is NOT the answer meaning Not true result as false
s = 1
t = 2
r = 3
print(not (t > s))# false bc the complier is saying not true
print(not(s> t))# true bc the complier is saying not false
print (not(s + t == r))#false bc s+t does equal 3, so not true
print(not(t+t ==r))#true bc 3 + 3 does not equal 3, so not false

print()
#MEMBER OPERATORS
#in memebership operator, in and out test all sequences like list and strings
#for list operator checks each element to see whether the element being searched for
#is within list.
#for string, operator checks the substring can be found in string

number = [1,2,3,4,5]
print(3 in number)#  true, since 3 is in list
print(12220 in number)# false


#can combine bolean operators,

print(2 and 3 in number)#true. 
print(1 and 2 and 3 in number)#true
print(6 and  9 and 1 in number)# true
print(6 and  1 and 9 in number)#false
print(6 and  9 and 9 in number)#false

print()

print(6 in number) and  (8 in number) and (1 in number) 
#print(6 in number) and (1 in number) and (3 in number) # false
#print(1 in number) and (8 in number) and (1 in number)# true
#print(6 in number) and (2 in number) and (6 in number)#false
#print(1 in number) and (2 in number) and (7 in number)#true

print()
#print(1 or 2 in number
print((1 or 5) in number)
print((9 or 1) in number)# why false is 2nd arg true
print((1 or 9) in number)

print()

print(6 not in number)
print(6 or 9) not in (number)#??

print()
word= "Im tired I want to go to sleep"

print("Im" not in word)#false, it is
print("Im" in word)#true it is
print("Bitcoin" not in word) #true
print("bitcoin" in word) #false
print("o" in word)#true
print("q" in word)#false


