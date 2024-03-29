# --------------
# Code starts here

# Creating class_1 and class_2 lists
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']
# Concatenating the class_1 and class_2 lists
new_class = class_1 + class_2

# Printing the new class lists
print("Students list:", new_class)
print("="*50)

#Adding the missing student
new_class.append('Peter Warden')

#Printing the updated list
print("Added the missing student:", new_class)
print("="*50)
# Removing the student
new_class.remove('Carla Gentry')

#The updated list
print("Removed the student:", new_class)

# Code ends here


# --------------
# Code starts here

courses = {'Math':65, 'English':70, 'History':80, 'French':70, 'Science':60}
print(courses)

marks_in_each_subject = courses.values()
total = sum(marks_in_each_subject)

print("Total marks", total)

percentage = (total*100)/500
print("Percentage scored by Geoffrey Hinton", percentage)
# Code ends here


# --------------
# Code starts here

mathematics = {'Geoffrey Hinton': 78, 'Andrew Ng': 95, 'Sebastian Raschka': 65, 'Yoshua Benjio': 50, 'Hilary Mason': 70, 'Corinna Cortes': 66, 'Peter Warden': 75}

topper = max(mathematics,key = mathematics.get)
print("Topper in class for Mathematics", topper)

# Code ends here  


# --------------
# Given string
topper = 'andrew ng'

# Code starts here

first_name = topper.split()[0]
last_name = topper.split()[1]

full_name = last_name + " " + first_name
certificate_name = full_name.upper()

print("This is to certify that", certificate_name, "has topped in Mathematics")
# Code ends here


