print("---------PROFILE----------")

name= input("What's your name? ")
age = input("How old are you? ")
height = input("Your height in cm? ")
student = input("if you are student put y else put n ")

print('\n')
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height in cm: {height}")

if (student == 'y'):
    print("Student: He is student")
elif(student =='n'):
    print("Student: He is not student")
else:
    print("Student: Unknown")

age_in5= int(age) +5 
print('\n')
print(f"In 5 years {name}, you will be {age_in5} years old. ")
print(f"Height in cm: {height}")