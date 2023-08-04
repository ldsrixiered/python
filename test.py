print('Hi how are you?')

what = input('what is your name?')

print('oh thats a great name')
print(what)

#FIRST

first = 'Rixie'
last = 'castro'
#you can use (f'{}') for inserting varialble 
print(first + last)
print (f'hello {first} {last}')
#or you can use like ('' +....+  ' ' ) to insert variable
print('hello ' + first + ' ' + last + ' ' + what)

#SECOND

print(first.upper())
#to upper case the string you have to add .upper() next after the variable
print(first.lower())
#to lower case the string you have to add .lower() next after the variable
print(first.capitalize())
#this will capitalize only the first letter of each word in the sentence
print(first.count('i'))
#counts i's in the string and returns an integer value