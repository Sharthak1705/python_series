animal = str(input("Enter the value is :")).strip().lower()

if animal == "dog":
    age = int(input("enter the age of dog:").strip())
    if age <= 2:
     print("puppy food")
    elif age > 2:
      print("adult dog food")
    else:
       print("invalid input")

else:
 print("Sorry , we only have food suggestion for other animal")