for x in range(1,21):
    if x == 4:
       print(f"{x} unlucky!") 
    elif x == 13:
        print(f"{x} unlucky!")
    elif x % 2 == 0:
        print(f"{x} is even")
    else :
        print(f"{x} is odd")