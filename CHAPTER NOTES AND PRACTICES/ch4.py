#BUILT IN FUNCTIONS
#python interpeter has number of functions and types that are always avaiable call built in functions
#they can be used anywhere in a code,w/i importation.

#input([prompt]) : this is optionally prints the prompt to the terminal. reads a line from the input and returns that line
#print() : prints the objects to the text stream file or the terminal .
#int() values into integers int(101010)binary in number

binarystring = "0011"
interger = int(binarystring, 2)
print(interger)

hexadecimalstring= "f"
interger = int(hexadecimalstring,16)
print(interger)

print()

#USER-DEFINED FUNCTIONS#
#functions that are written by the user, to aid them in achieving goal.Main goal is to help org.
#our programs into logical fragments that works together to solve a specific part of our problem.
#The syntax of Python fuction below

# def function_name(paramater_one,paramater_two)                    
  #logical goes here                                                 
  #return

#To define a function-
#use the 'def' keyword, followed by the function name. 
#add the paramater (if any) to the function w/i the paratheses. End the function definition with a full colon :
#finally, use 'return' keyword to return the output of the function.
#This is optional and is not included, the function auto returns 'none;

#Write the logical-


#GLOBAL AND LOCAL VARIABLES
#variables that are denfined inside a function body are called local variables,
##as they are only accessible inside the finction. local scope.

#variables that are defined outside of a finction body are Global, as they are accessible both outside and in
# of functions. Global scope.

# Global variable
count = 20

def increment_counter():
    # Local variable
    count = 5
    print(f"Local count: {count}")          ####COPILIOT EXAMPLE :(
    
def use_global_counter():
    global count
    count += 1
    print(f"Global count: {count}")

# Call the functions"
    increment_counter()
    use_global_counter()
    duse_global_counter()

print()

def summation(first,second): #once a variable is defined, it follows it for the rest of the forumla 
    total = first + second                                 ##SPACES AND LINEUPS MATTERS##
    print("the total is " + str(total)) #str allows you to convert data(10 and 20 in this example) into string
                                      #note int is needed b/c it convert the value of (total) in intergers
summation (10,20)

#return statement is required if you need to use the result of calling a 
#function for any further processing in your code.

def summation(first, second):               
    total=first + second                         # return produces this -> the total is 30
    return total                            
outer_total = summation(10,20)*2
print("double to total is "+ str(outer_total))  # print produces the string of -> the double to total is 60

#the summation function returns the sum of the passed-in values. 
#This returned value is then multiplied by two and assigned to the outer_total variable. 
#This way, the function has, in essence, abstracted away the operation of summing the two numbers.
print()

def concatenate_strings(a,b):
    return str(a) + str(b)

# Test the function                      #okok so by adding return, your passing the forumla str for string
result = concatenate_strings(123,456)   # to the numbers 123 and 456 which you normally can't concatenate
print(result)  # Output: '123456'        # normally you have to do something like 

                                         #                                        list2 = [456] 
                                         #                                 combine_list = list1 + list2
                                         #                                 print(combine_list) to [123,456]                                                                 
print()

#USING MAIN#

#Most other programming languages (for example, Java and C++) require a special function, called main(), 
#which tells the operating system what code to execute when a program is invoked. This is not necessary in Python,
# but you will find that it is a good and logical way to structure a program.

#before the Python interpreter executes our program, it defines a few special variables. One of them is __name__, 
#and it will automatically be set to __main__ if our program will be executed by itself, in a standalone fashion.

#However,if our program will be imported by another program, then __name__ will be set to the name of that other program. 
#We can easily determine whether the program is standalone or is being used by another program as an import. Based on that,
# we can decide to either execute or exclude some of the code in a program.


def summation(first, second):               
    total=first + second                       
    return total                            
outer_total = summation(10,20)*2
print("double to total is "+ str(outer_total))

#FUNCTION AGRUMENT#

#paramater are the informartion that needs to be passed to the function for it to do its work.Although
#paramater are commonly referred to as arguments, arguments are thought of more  as the actual values or 
#references assigned to the paramater variables when the a function is called at runtime. 
#Arguments are to functions as ingredients are to recipes.Types of Arguments:
#  
# Required, Keyword, Default and a variable number of arguments
#  
# REQUIRED ARGUMENTS# 
# arguments to have to be present when calling a function. also have to be in correct order for it to function to work.
def division (first,second):
    return (first/second)           #You have to pass first and second for the function to work. also have to pass
                                   #the argument in correct order, as switching them will yield completely different results
quotient = division(10,2)
print(quotient)                      #fyi meaning of quotient is dividing one quatity by another

print()

#KEYWORD ARGUMENT#
#if necessary, you can call all the paramaters in the right order, you can use keyword arguments in your function call.
#Can use these to indentify the arugments by their paramater name.

def division (first,second):
    return first/second
quotient = division (second=2,first=10)  # keyword arugment was used by calling the paramaters of second and first
print(quotient)

#DEFAULT ARGUMENTS

#Default arguments are those that take a default value if no argument value is passed during the function call.
# You can assign this default value with the assignment operator, =

def division(first,second):
    return first/second
quotient = division(10, 5)
print(quotient)

#Note that even if the argument named second has a default value, you can still pass a value to it, 
#and this passed value will override the default value. This means that the function will promptly 
#ignore the default value and use whatever value you passed to it.

 
#ANONYMOUS FUNCTIONS

#Anonymous functions in Python are also called lambda functions.This is because they use the keyword lambda 
#in their definition. Anonymous functions are so called because, unlike all of the other functions that we 
#have looked at up to this point, they do not require to be named in their definition. The functions are 
#usually throwaway, meaning that they are only required where they are defined, and are not to be called in 
#other parts of the codebase.The argument list consists of a comma-separated list of arguments, and the expression
#is an arithmetic expression that uses these arguments. You can assign the function to a variable to give it a name.

#The true power of anonymous functions can be seen when they are used in combination with 
#the map(), reduce(), or filter() functions.

map(funtc,)

#The first argument, func, is the name of a function, and the second, iterable, 
#is a sequence (for example, a list). map() applies the func function to all of the elements of the 
#iterable sequence. It returns a new list, with the elements changed by func.