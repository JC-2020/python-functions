# Write a function that accepts two arguments: a name and a subject.
# The function should return a String with the name and subject interpolated in. 

# Create the function
def madlib(name, subject):
    return f"{name}'s favorite subject is {subject}."
    
# Ask user to input name and subject
name = str(input("What is your name?\n> "))
subject = str(input("What is your favorite subject?\n> "))
# Print function 
print(madlib(name, subject))