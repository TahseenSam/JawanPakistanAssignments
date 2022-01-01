import sys
from datetime import datetime
# PROGRAM 1 - PRINT TWINKLE STAR

print("\nProgram 1\n")
print('TWINKLE TWINKLE, LITTLE STAR,')
print('\tHow I wonder what you are!')
print('\t\tUp above the world so high,')
print('\t\tLike a diamond in the sky,')
print('TWINKLE TWINKLE, LITTLE STAR,')
print('\tHow I wonder what you are!')

# PROGRAM 2 -GET PYTHON VERSION
print("\nProgram 2 - Python Version\n")
print(sys.version)

# PROGRAM 3-DISPLAY CURRENT DATE AND TIME
print("\nProgram 3\n")
d = datetime.now()
print(d.strftime('%d-%m-%Y %H:%M:%S'))

# PROGRAM 4- TAKE RADIUS OF CIRCLE ,PRINT AREA
print("\nProgram 4\n")
pi = 3.14
radius = float(input('Enter Radius Of Circle : '))
print('Area Of Circle : '+str(pi*radius**2))

# PROGRAM 5 - PRINT F-NAME AND L-NAME IN REVERSE ORDER
print("\nProgram 5\n")
fName = input('Enter Your First Name : ')
lName = input('Enter Your Last Name : ')
print(lName+' '+fName)

# PROGRAM 6-PRINT ADDITION OF TWO NUMBERS
print("\nProgram 6\n")
n1 = int(input('Enter 1st Number : '))
n2 = int(input('Enter 2nd Number : '))
print(n1+n2)
