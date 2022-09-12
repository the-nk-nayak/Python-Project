import random
random_number=random.randint(1,20)

i=1
while i<=8:
    user_value= int(input("Enter the Number : "))
    if random_number==user_value:
        print(f"You won the game you will take{i}")
        break
    elif user_value<random_number:
        print("please rnter the large number")
    elif user_value>random_number:
        print("please enter the smaller value")

    i=i+1