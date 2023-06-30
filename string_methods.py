# str.lower(): Converts all characters in a string to lowercase.

greeting = "Hello, World!"
lowercase = greeting.lower()
print(lowercase)  

name = "NSE"
edited_name = name.lower()
print(edited_name)

print(name)


# str.upper(): Converts all characters in a string to uppercase.

greeting = "Hello, World!"
uppercase = greeting.upper()
print(uppercase) 
print(greeting)

# str.strip(): Removes leading and trailing whitespace from a string.

greeting = "   Hello, World!   "
stripped = greeting.strip()
print(stripped)  

print(greeting)

print(len(greeting))
print(len((stripped)))


#with arguments
greeting = ",,Hello, World!,,"
stripped = greeting.strip(',,')
print(stripped)  
print(greeting)




# str.lstrip() only strips from the leading which is the left side of the string 

greeting = "    Hello, World!"
new_greeting = greeting.lstrip()
print(new_greeting)
print(greeting)



# str.rstrip() only strips from the right side
# string.rstrip([characters])

greeting = "...Hello, World!..."
new_greeting = greeting.rstrip('...')
new_greeting2 = greeting.lstrip('...')
print(new_greeting)
print(new_greeting2)


# replace(): Replaces all occurrences of a substring with another substring. 
# str.replace(old, new, [count])



string = "Hello, World! World"
new_string = string.replace("Hello", "People")
print(new_string)  


string = "Subscribe to Learn-In, Learn-In has cool videos"
new_string = string.replace("Learn-In", "channel")
print(new_string)







# Method chaining
# Method chaining in Python refers to the technique of calling multiple methods on an object in a single statement.

string = "  hello, world!  "
chained_methods = string.strip().replace("hello", "hi").upper()
print(chained_methods)

