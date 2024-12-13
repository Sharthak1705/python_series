weather = str(input("Enter The value:"))

if weather == "Sunny":
    activity = "It's a beautiful day, isn't it?"
elif weather == "Rainy":
    activity = "Don't forget your umbrella!"
elif weather == "Snowy":
    activity = "Enjoy the snow, but stay warm!"
else:
    activity = "I'm not sure what the weather is like today."

print("Today's weather is:", activity)
