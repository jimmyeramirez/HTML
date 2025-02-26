#Control statements lik "if and "while"control the flow of the program
#achieves this by changing the controlling excuting part of the code. can be use repeatlly and
#conditionally excute some code. Think of control statements as traffic officer at junction who only
# lets you in "if" the exit is clear, checking whether the exit is cleared.
#Two main types of control statements are "if" and "while"

# "if" statement allows to excute a block code if a condition is true. Otherwise it can run an 
#alternative block code in the "else" clause. The "else" clause of an "if" statement is optional.
# can have multiple "if" statements that check for multiple conditions one after the other and excute 
#  different block of code when various conditions are true. Would use "elif" statment if a combination
#  # of "else" and "if" is used. it enables a braoder comparison scope through chaining multiple "if"
#  
"""example of basic if statement"""

#after writing first control statement, must end with : to promp the
#correct formatting


 #multiple chain control stament "if", 


number = 20
if number > 12:                            #notice the indention in print
    print("the number is positive:")      #its part of the command.
                                          #b/c 20 is greater than 12, the complier prints
elif number <12:                          # the string for if. If is true. doesn't go to next arg.                         
    print("the number is negative:")      # if "number=" was 9, it makes the "if" statement false goes to next arg
                                          # following the "elif" forulma (number<12) as true
                                          # making it the complier print the number is negative
else:                                     #if number= was 12 it was print out "the number is "  or                                      # since "if" and "elif" 
    print("the number equals whatever.")  # both "if" and "elif" are false, print else string

#single "

ex = 1

if ex > 10:
    print("ex is greater 10")  # single "if" if ex is > #, it's print that print string
                                 #if ex is not > #, making the statement false, it
else:                             #will print the else print string
    print("ex is less then 10")



print()



sentence = "ducks can fly"
makesense= len(sentence)

if "bitcoin" not in sentence:
    print("word enter in formula is not in sentence")

elif makesense < 1:
    print("sentence has less letters than whatever number was entered in formula")

else:
    print("search word is not in sentence and sentence has more letters than number entered in elif formula ")
    #so if searched word in "if" is not in sentence and 
    #if the # of characters in "ducks can fly" is < the number enter in "elif"
    # we print "else" string
  
    
print()
#WHILE STATEMENT
#while statement allow you to excute block of code repeatedly as long
# as condition remains true. 
# as long as condition X remains true, execute this code.

#While statments can also have "ELSE" clause that will be excuted once when
#condition x is no longer true.
#As long as X remains true, execute this block of code, else, 
#execute this other block of code immediately when that condition is no longer true.

  
countdown = 20

while countdown >0:#CAUSES THE WHILE TO LOOP, BC -= SUBTRACTS A VALUE(countdown 20) FROM A VARAIBLE(-= 1) UNTIL THE STATMENT WHILE COUNTDOWN >(0) IS FALSE, then prints liftoff
    print(countdown)
    countdown -= 1  # Decrement the countdown by 1

print("Liftoff!")      

print()

number = 8

while number < 10:
    print(f"Current number: {number}")
    number += 2  # Add 2 to the number

print("Final number:", number)


#difference bt if and while
#
#The main difference between an if and a while statement 
#is that an if statement gives you the opportunity to 
#branch the execution of code ONCE based on a condition. 
#The code in the if block is only executed once.


#A while statement, however, gives you the opportunity to 
#run a block of code MULTIPLE times as long as a condition
# evaluates to true. This means that a while statement will,
# for example, execute a computation as long as
# value A is greater than value B and only proceed with the 
# program flow when A is no longer greater than B


#python loops are a way to execute a specific block of code several times. In particular, 
#loops are used to iterate or loop over what we call iterables.
#iterable is an object in programming that contains a sequence of elements and allows you to 
#traverse through each element one at a time. 
#In Python, for example, common iterables include lists, tuples, dictionaries, and sets. 
#You can loop through an iterable using a for loop or other iteration methods.

#THE FOR LOOP#

#The for loop in Python is also referred to as the for..in loop
#This is because of its unique syntax that differs a bit from for loops in other languages.
#A for loop is used when you have a block of code that you would like to execute repeatedly 
#a given number of times. For example, multiplying an iterable value, or dividing the value 
#by another if the iterable value is still present in the loop.

#The loop differs from a while statement in that in a for loop, 
#the repeated code block runs a predetermined number of times, 
#while with a while statement, the code runs an arbitrary number of times 
#as long as a condition is satisfied.

#the example below is an iterable of a list. fruits = the list
# Your basically telling the complier for the values in 
# the list named fruits, print each fruit out until no more fruits.

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:   
           #FRUIT IS THE FORUMLA. WHEN YOU PRINT THE FORUMLA "FRUIT"
           #YOUR ASKING THE COMPLIER TO PRINT OUT THE VALUES "IN" THE LIST "FOR" FRUITS
 print(fruit)


print()

numbers = [1, 2, 3, 4, 5]
# Iterate over the list of numbers
for number in numbers:    #NUMBER FORMULA "FOR" EACH # "IN" THE NUMBERS LIST
    square = number * number #SQUARE FORMULA IS EQUATIONING TO THE PRODUCT EACH # X IT SELF (square of 2)
    print(f"The square of {number} is {square}") #PRINT THE STRING SAYING "THE SQUARE {# IN NUMBERS LIST}
    #IS {THE PRODUCT OF EACH# X ITSELF}

    #reminder* the f allows you to embedd {variables} in string 
    #n this example, the list numbers is an iterable. 
    #The for loop iterates over each element in the list, 
    #calculates the square of each number, and 
    #prints out the result.

print()
print()
      #RANGE FUNCTION#

# range FUNCTION IS A BUILT-IN FUNCTION THAT GENERATES A LIST.MOSTLY USED FOR for LOOPS.
#range IS USED WHEN YOU WANT TO PERFORM AN ACTION FOR A PREDETERMINED NUMBER OF TIMES,WHERE
#YOU MAY OR MAY NOT CARE ABOUT AN INDEX
#(INDEX IS A VARIABLE MEANT TO INDICATE A POSITIONOF ELEMENTS IN LIST, ARRAY,OR STRING)
#FOR INSTANCE, YOU CAN USE range TO FIND EVEN #s BT 0 AND 100.PYTHON WOULD PRINT OUT ALL EVEN #s
#INCLUDING 100, EVEN THOUGH ITS AN EVEN NUMBER.
#start- THE STARTING # OF A SQUENCE
#stop- MEANS GENERATE #s UP TO BUT NOT INCLUDING THIS #
#step-# THIS IS THE DIFFERENCE BT EACH #s IN A SQUENCES
# WHEN A PARAMETER IS ENCLOSED WITH BRACKET[] IN THE FUNCTION, IT MEANS THAT THAT PARTICULAR
#PARAMETER IS OPTIONAL WHEN YOU ARE CALLING FOR THE FUNCTION.
#THIS MEANS THAT THE ONLY REQUIRED PARAMETER WHEN CALLING FOR THE range FUNCTION IS THE 
##stop PARAMETER, AND THE DEFAULT CALL TO THE FUNCTION CAN HAVE JUST THAT ONE PARMETER.
  
for numbers1 in range(10): #print #s from 0 to 9
     print(numbers1)

print()

for numbers2 in range(5,10):# prints list of #s beginning at 5 up to 9
    print(numbers2)

print()

for numbers3 in list(range(10,100,20)): #prints list of #s starting at 10 up to 100 in emcrements of 20
    print(numbers3)                     #10 emcrements of 20, next # is 30, then 50, 70, 90

print()


for num in range(1,11):
    print(num, 'squared is', num * num)


print()

numbers = [1,2,3,4,5,6,7,8,9,10]
for num1 in numbers:
    square= num1*num1
    print(num1,"squared is",square)

print()

#NESTING LOOPS#

#DEFINED AS PLACING LOOPS INSIDE OF LOOPS.IMPORTANT IS YOU NEED TO ACCESS DATA INSIDE A COMPLEX DATA
#STRUCTURE

# Nested for loop to create a multiplication table
for i in range(1, 6):  # Outer loop
    for j in range(1, 6):  # Inner loop
        product = i * j
        print(f"{i} x {j} = {product}")
    

print()

#BREAKING LOOP#
#When running loops, we might want, because of an external factor, to interrupt or 
#intervene in the execution of a loop before it runs its full course. 
#BREAK CONTINUE PASS

#BREAK STATEMENT
#The break statement allows you to exit a loop based on an external trigger. 
#This means that you can exit the loop based on a condition external to the loop.
# This statement is usually used in conjunction with a conditional if statement.

#loop over all numbers from 1 to 10

for number in range(1,11):                        #"for" the values from the NUMBER list "in" the "range"
      #if the numbers is 4, exit the loop         #[1,10],"if" the value from the NUMBER list == 4, "break"
      if number == 4:
          break                                                                    
                                                   
     #calculate the product of number and 2 
      product = number * 2                        #from the forumla of product being the values of the Numbers list
                                                  # X 2      
      print(number,'*2 = ', product)              #Print the string of the values in the number list "*2=" and the product formula.
         
print("loop completed")                           #print the string "loop completed" well loop is done


print()

#THE CONTINUE STATEMENT#
#The Continue Statement allows you to the skip over the part of a loop where an external condition
#is triggered, but then goes on to complete the rest of the loop. This means the 
#current run of the loop will be interrupted , but the program will return to the
#top of the loop and continue execution from there.
#As with break statement, the continue statement is usually used in conjuction with a 
#conditional "if" statement.

#loop over all numbers from 1 - 16
for number in range(1,16):
    #if the number is 4 , continue the loop
    if number == 4:
        continue
    if number == 11: #adding this with "break" is trying the complier in addition to skipping over #4
       break         # break at #11, printing to 10
#calculate the product of number and 2
    product = number * 2
    #print out the product in a friendly format
    print(number, "* 2=", product)

print("end of loop")

print()
#PASS STATEMENT#
# the pass statement allows you the handle external triggers conditions w/o affecting the execution
# of the loop; the loop will continue to excute as normal unless it hits a break or continue statement
# somewhere later in the code.pass is used in conjuction of if statement

for number in range(1,20):
    #if the number is 4 , continue the loop
    if number == 4: #adding this with "break" is trying the complier in addition to skipping over #4
        continue
    if number == 18:C
       break         # break at #18, print up to 17
    if number == 10:  # basically does nothing
       pass
#calculate the product of number and 2
    product = number * 2
    #print out the product in a friendly format
    print(number, "* 2=", product)
    print() #adding print() here separates the lines in each result
print("end of loop")

