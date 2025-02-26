from locale import bind_textdomain_codeset, format_string


s = """bitcoin is all"""
print(s[-14],s[-13],s[-12],s[-11],"h",s[-14],s[-13],s[-12],"ches")


sleep="i need more sleep"
print(sleep[0:6])
print(sleep[-15:-10])
print(sleep[3:])
print(sleep[:3])

dog = 'animals*'*8
print(dog)


who = """ 'triple quotes creates multistring lines 

a
l
s
o 

quotes can be inside of a value' """
print(who)

answer = "the number of character in this value is given when you print((len(answer))"
print(len(answer))

how='concatenate' 
do=' strings'
you=" is when you"
combine=' add multiple +'
multiple_variables=' b/w variables in print job'

print(how+do+you+combine+multiple_variables)

how = "create a variable like normal then a second one named format_string, " 
format_string = f"{how} have format_string equaling f and then have f state another value, add the first variable witin curly braces, you can combine two values togther"

print(format_string)


age=50
years=10
str_fortmat=f"in {years} I will be {age}, fuck"

print(str_fortmat)

format_string = f"in {years} {you} will die from old age"
print(format_string)


crypto='btc' 
own = 7
straight_format = f"my favorite crypto is {}, I own {} coins"format(crypto, own)
print(straight_format)


