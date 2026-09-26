name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

print("\nEnter marks out of 100:")

maths = float(input("Maths: "))
python = float(input("Python: "))
english = float(input("English: "))

total = maths + python + english
percentage = total / 3

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("\n====================================")
print("          STUDENT RESULT")
print("====================================")
print("Name       :", name)
print("Roll No.   :", roll_no)
print("Maths      :", maths)
print("Python     :", python)
print("English    :", english)
print("Total      :", total, "/ 300")
print("Percentage :", round(percentage, 2), "%")
print("Grade      :", grade)
print("====================================")
