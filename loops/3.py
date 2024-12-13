#using break in loop

number = 3
count =0

for i in range(1, 11):
    if i == 5:
        continue
    print(number , 'x',i,'=',number * i)


