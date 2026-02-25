print("Hello, World!")


print("*" * 10)

# Types of variables
# Strings

course = "Python Programming"
print (len(course))
print(course[0])
print(course[-3])
print(course[0:6])

print (course.upper())
print (course.lower())
print (course.title())
print (course.strip())
print (course.find("P"))
print (course.replace("P", "J"))
print ("python" in course)

# numbers

print(10 + 3)  # addition
print(10 - 3)  # subtraction
print(10 * 3)  # multiplication
print(10 / 3)  # division
print(10 // 3)  # floor division
print(10 % 3)  # modulus
print(10 ** 3)  # exponentiation


# operator precedence
x = 10
x += 3  # x = x + 3
print(x)

# working with numbers

print(round(2.9))
print(abs(-2.9))  # IT RETURNS THE ABSOLUTE VALUE OF A NUMBER
print(pow(2, 3))  # IT RETURNS THE VALUE OF 2 TO THE POWER OF 3
print(max(2, 3, 4))  # IT RETURNS THE MAXIMUM VALUE AMONG THE ARGUMENTS
print(min(2, 3, 4))  # IT RETURNS THE MINIMUM VALUE AMONG THE ARGUMENTS

x = input("x: ")
y = int(x) + 1  # IT CONVERTS THE STRING INPUT TO AN INTEGER AND THEN ADDS 1 TO IT
print(f"x: {x}, y: {y}")

# int(x) #IT CONVERTS THE STRING x TO AN INTEGER
# float(x) #IT CONVERTS THE STRING x TO A FLOAT
# bool(x) #IT CONVERTS THE STRING x TO A BOOLEAN
# str(x) #IT CONVERTS THE INTEGER x TO A STRING
