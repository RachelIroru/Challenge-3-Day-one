
input = input("Enter year of birth")
age = int(input)
if age < 18:
    print ("Minor")78
=======
input = input("Enter year of birth") //prompts the user to enter their date of birth
age = int(input) //user should input variable type interger
if age < 18: //condition 
    print ("Minor")

else:
    if age > 18 and age < 37:
        print("Youth")
    else:
        print("Elder")
