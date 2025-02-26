#CHAPTER 5 LIST AND TUPLES

#A list is a data structure that holds ordered collections of related data.List are known as 'arrays' in other programming language
# like Java and C++. List in Python are more flexible and powerful than tradditonal arrays of other languages.
#example of this power is that "lists" do not have all to be all the same type. List can be string text,intergers or
# even other lists. 

# The main properties of List#
# 1) they are ordered. 2)They contain objects of arbitrary type. 3)The elements of list can be accessed by an index   (meaning you can call element by location in list)
# 4)arbitary nestable, that is,they can contain other lists as sublist  5)They have variable sizes                                       ex of index# # List of fruits
#6)They are mutable this is the elements in a list change be changed                                                                     #fruits = ['apple', 'banana', 'cherry']
#access elements using their index
                                                                                                                                           #print(fruits[0])  # Output: 'apple'
                                                                                                                                           #print(fruits[1])  # Output: 'banana'
                                                                                                                                           #print(fruits[2])  # Output: 'cherry'
#TUPLES
# are used to hold together multiple related objects. Similar to the list in data types, but differ in that they are
# sequence of data types but differ in that they dont have all the functionality afforded by lists. The key difference
#  bt lists and tuples is that you cannot change the elements of tuples once they are set.This property of Tuples is 
#  is called IMMUTABILITY.
#  
#LIST SNYTAX#
#list are created in several ways. The simpliest of them enclose the elements of the list in [] square brackets.
#empty list [ ] - no elements
#list containing number [1,2,3] -contains numbers
#list with mixed types ["one",2,"three",["five,6]] contains numbers, strings and sublists inside it
#
#LIST METHOD     
#The list data types has some built-in methods that can be used with it. method as follow:
#1) list.append(item) 2)list.extend(iterable) iterable is any object capable of returning its elements one at a time   ex of iterable    fruits = ['apple', 'banana', 'cherry']
#3)list.insert(index,item)   4)list.remove(item)   5)list.pop([index])   6)list.clear()                                                  #for fruit in fruits:
#7) list.index(item[,start [, end])  8)list.count()  9)list.sort(key=None, Reverse=false)
#10)list.reverse()  11)list.copy
#

##LIST.APPEND(item) 
#method adds a single item to the end of the list. doesnt return new list, only modify original
things =["first"]                                         # can only add one word with append
things.append("another thing")                            # would have to create new list and extend if more than one
print(things)#['first',"another thing"]                  #  iterable


print()
#list.extend(iterable) 
#method takes one argument, which should be iterable data type. In then extends the list
# appending the all the items from the iterable to the list. ex extend a list with another word
things =['first','another word']
others =["third", "fourth"]                        # have to create a new list of iterable data type if more than one.
things.extend(others)
print(things) # ['first','another word','third.'fourth']

print()
# What happens if you passed a string with extend method
things = ["first"]
things.append("another thing")     #remember append treats it as one element to the list.
#print(things) gets below results
#things['first','another thing']
things.extend("another thing")
print(things) #['first',another thing','a','n','o' until another thing is spelt out]
               #this happens because thing.extend("another thing") as an iterable string and not a iterable list
               #remember, a list contains data point that if were ['words'] or [numbers](notice quotes for words) each point are fixed 
               #a string is essentially a SEQUENCE OF CHARACTERS. Each character in the string can be accessed individually, and strings are iterables, 
               #which means you can loop through each character one at a time.TUPLES WILL ALWAYS HAVE EITHER ( ) OR ,,,, OR BOTH

print()
#list.insert(index, item)
#The list.insert(index, item) method (as the name suggests) inserts an item at a 
#given position in a list. The method takes two arguments, index and item. 
#The index is the position in the list before which to insert the item defined in the second argument. 
#Both arguments are required.

things = ["second"]
#print(things) -> ['second']
things.insert(0,"first") #-> you're telling the complier to place(index) the string in the 0 position
print(things) #-> ['first','second'] 

print()
#list.remove(item)
#The list.remove(item) method removes from the list the first 
#item whose value matches the argument item thats passed

things=["first","second"]
#print(things)->['first','second']
things.remove("second")  #-> telling complier to  remove the string "second"
print(things) #-> ['first'] 

print()

stuff = ["bitcoin","corn","money","honey"]
stuff.insert(2,"xrp")
stuff.append("coin")
numberstuff=[1,2,3,4,5]
stuff.extend(numberstuff)
otherstuff=("trying to much")
stufflen=len(otherstuff)
finalstuff=(stuff) + [stufflen *8]*2

print(finalstuff)

print()

#list.pop([index])
#The list.pop([index]) method removes the item at the given index of the list, and returns it. 
#The index is an optional argument, and if it isnt passed in, the method will remove the last item in the list.
things=['first','second','third',]

secondthing = things.pop(1)   #we created a second agrument called secondthing. 
                                   #Remember to use( )parathese bc we are
print(secondthing)                  #are defining the position of 1.[ ] would be creating a list       
print(things)                       #secondthings equals the list called 'things' popping or remove
                                    #the ELEMENT in the 1 position from the list called 'things.
                                    #the element in the 1 postion is the string 'second'. 
                                    #0 is a positionthe argument things has 3 position from 0-2.
 #2nd argument of secondthing will print the element string of 'second'  
                                 # with no brackets ,no paratheses no commas, and no quotes.
 #print(things)  prints the modified argument ['first,'third']           

secondthingwithoutindex = things.pop()                            
print(secondthingwithoutindex)
#not using an index          
#pops out the last            
#element                     

                            
print()
 
#list.clear()
#As the name suggests, the list.clear() method removes all items from a list.
# An alternative to this method would be del list[:].

mylist=[1,2,3,4,5]
list.clear(mylist)
print(mylist)    #removes everything from the list printing just []

print()

#he list.index(item [, start [, end]]) 
#method returns the index of the first item in the list whose value is item.
#The parameters start and end are optional, and they indicate the position in the list at which the 
#search for said item should start and end,respectively. Again, the very beginning of the list is index zero. 
#The index at the end of the list is one less than the length of the list.
# Define a list of elements
my_list =        ['a','b','c','d','e','b','f','g','h','i','f','k','l','m','o','p']
#element position  0  1   2   3   4   5   6   7   8   9  10   11  12  13  14  15 / 15 position and 16 elements
# Find the index of the first occurrence of 'b'
index_1 = my_list.index('b')
print(index_1)  # Output: 1

# Find the index of 'b', starting the search from index 2
index_2 = my_list.index('b', 2)   # two b's in the list. and start from index 2 which is C forward
print(index_2)  # Output: 5       # until you find the second be which is in location 5.

# Find the index of 'f', within the range of index 7 to 11
index_3 = my_list.index('f',7,11 )  # 2 f's looking for f's and start from 7(g) to (11)
print(index_3)  # Output: 10

print()
#list.count(item)
#The list.count(item) method returns the number of times the 
#given item occurs in the list.
total=my_list.count('b')
print(total)              #list count only counts one element at a time to do multiple
                          # have to create a dicttionary
print()
# Define a list and elements to count
my_list = ['a','b','c','d','e','b','f','g','h','i','f','k','l','m','o','p']
elements_to_count = ['b', 'f']

# Use dictionary comprehension to count elements
counts = {item: my_list.count(item) for item in elements_to_count}

print(counts)  # Output: {'b': 2, 'f': 2} 

#question to copilot was why item has item: and item =      : vs =  
#Use : in dictionary comprehensions to separate keys and values and in function definitions 
#to indicate the start of the function body.
#Use = for assignment, to assign values to variables.

print()

#The list.sort([key=None|function, reverse=True|False]) 
#method sorts the items of the list. The key and reverse parameters are optional. 
#The key parameter specifies a function to be called on each list element prior to making comparisons.
# A common use for this is if you have a list of lists and you want to sort on an element of the sublists. 
# If you wish to not specify a key, you can leave out this parameter or specify key = None. 
# The reverse parameter tells the method to sort in ascending (False) or descending order (True). 
# If this parameter is not specified, the default sort order is ascending.


newlist =["Bitcoin","Nikolai","lily","jimmy","mSTR","aTHENA","baby","Andy"]
#newlist.sort()   
                 # your modifying the orignial this way.
                 # with no key enter, list gets sorted from Upper to lower case 1st, then a-z          
#print(newlist)   #Andy,Bitcoin,Nikolai,aTHENA,baby, etc             
print()

#sort= sorted(newlist,  reverse =True)   # if you didn't want to modify the orignial list
                                                        #True or False has to be capts.false ascends, true descends
                                                        # you have to use sorted() method- not discussed in
newlist5 =["Bitcoin","Zebra","Nikolai","lily","jimmy","mSTR","aTHENA","baby","Andy"]
#understanding the sorted/sort key= , reverse= 
sort1=sorted(newlist5,key=str.upper,reverse=False) #Andy,aTHENA,baby,Biction,jimmy,lily,Zebra
sort2=sorted(newlist5,key=str.upper,reverse=True)  #Zebra,Nikola,mSTR,lily,jimmy,Bitcoin,baby,aThena,Andy
sort3=sorted(newlist5,key=str.lower,reverse=False) #Andy,aTHENA,baby,Bitcoin,jimmy',lily,mSTR',Nikolai,Zebra
sort4=sorted(newlist5,key=str.lower,reverse=True)  #Zebra,Nikolai,mSTR,lily,jimmy,Bitcoin,baby,aTHENA,'Andy
print(sort1)
print(sort2)
print(sort3)
print(sort4)

print()

#The list.reverse() 
#method reverses the elements of the list.
newlist6 =["Bitcoin","Zebra","Nikolai","lily","jimmy","mSTR","aTHENA","baby","Andy"]

newlist6.reverse()  # modifys the original list of newlist6
print(newlist6)

print()

#The list.copy() method returns a shallow copy of a list.
#A shallow copy means that if you modify either list, 
#the original or the copy, only that list is modified.

# Define the original list
original_list = [1, 2, [3, 4], 5]

# Create a shallow copy of the list
copied_list = original_list.copy()

# Modify the copied list
copied_list[0] = 10  #adds 10 in the 0 position 
copied_list[2][0] = 30 # adds 30, in the 2 second position elements which are the [] and  in the 0 position within []

# Print both lists
print("Original List:", original_list)  # Output: Original List: [1, 2, [30, 4], 5]
print("Copied List:", copied_list)     # Output: Copied List: [10, 2, [30, 4], 5]

#tuples

