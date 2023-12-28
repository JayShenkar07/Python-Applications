Books={"C":"Dennis Ritchie","C":"Dennis","C++":"Bajarne Stroustope", "Java":"Gosling", "Python":"Guido Van Russom "}

print(Books)
print(type(Books))

language=Books.keys()   #.keys() is a method to separate out all the keys 
author=Books.values()   #.values() is method to separate out all the values

print(language, end=" ")
print(" ")
print(author, end=" ")