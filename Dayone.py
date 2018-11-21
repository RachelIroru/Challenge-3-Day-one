input = input("Enter year of birth")
age = int(input)
if age < 18:
    print ("Minor")78
else:
    if age > 18 and age < 37:
        print("Youth")
    else:
        print("Elder")