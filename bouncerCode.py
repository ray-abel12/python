age = input("please enter your age ")
age =int(age)

if age:
    if age >= 18 and age < 21:
        print("you are can enter but have a wristband")
    elif age > 21:
        print ("you can enter and enjoy")
    else:
        print("you are too young ")
