grade = int(input("Enter the value: \n"))

if grade>=101:
    print("Grade is not exist")
    exit()
    
if grade>=90:
    print("Grade is A")
elif grade>=80:
    print("Grade is B")
elif grade>=70:
    print("Grade is C")
elif grade>=60:
    print("Grade is D")

else:
    print("Grade is F")
    print("Grade in",grade,"%")