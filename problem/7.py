size = str(input("Enter the size of coffee (Small/Medium/Large): ")).strip().capitalize()
extrashot = str(input("If extrashot is (Yes/No): ")).strip().lower()


if size in ["Small", "Medium", "Large"]:
    if extrashot == "yes":
        coffee = size + " Coffee with an extra shot"
    else:
        coffee = size + " Coffee"
    print("Order of coffee:", coffee)
else:
  print("Invalid size")
