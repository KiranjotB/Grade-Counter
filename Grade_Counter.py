print("Welcome to the grade counter! This program will allow you to enter in a list of grades of your choice to help you determine the amount of grades in the A-F scale.")

#n = float(input("Please enter a numerical grade (-1 to terminate):"))
numA = 0
numB = 0
numC = 0
numD = 0
numF = 0

#n=float(input("Please type in a score (-1 to terminate):"))
n = -2
while(n != -1):
		try:
				n = float(input("Please type in the next grade:"))
				if n<0 and n!= -1:
						print("This is an invalid entry. Please enter in a new grade:")
				else:
						if(n >= 90 and n < 100):
								numA += 1
						elif(n >= 80 and n < 90):
								numB += 1
						elif(n >= 70 and n < 80):
								numC += 1
						if(n >= 60 and n < 70):
								numD += 1
						elif(n >= 0 and n < 60):
								numF += 1
		except ValueError:
				print("This is an invalid entry. Please enter in a new grade:")
max_grade = max(numA, numB, numC, numD, numF)

most_common_grades = []

#In lines 29-43 we are appending the letter A to the list only if numA is equal to the maximum of them for example. If most of the grades are A's, then the list will follow the code and output that result.

if max_grade == numA:
		most_common_grades.append("A")

if max_grade == numB:
		most_common_grades.append("B")

if max_grade == numC:
		most_common_grades.append("C")

if max_grade == numD:
		most_common_grades.append("D")

if max_grade == numF:
		most_common_grades.append("F")


#Checking if there is only 1 winner otherwise it is a tie.
if len(most_common_grades)==1:
		print("There are more", most_common_grades[0], "grades.")
else:
		print("It is a tie", most_common_grades)

