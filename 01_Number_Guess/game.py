import random 

low,high=1,100
num=random.randint(low,high)
attempts=7

print("=====================================================")
print("-----------Welcome to Number Guessing Game-----------")
print("=====================================================")
print(f"\n Guess A Number between {low} and {high} \n")

#_Game loop 
while attempts>0:
    try :
        user=int(input("Guess Number : "))

        if user>num :
            print("Too High")
        elif user<num :
            print("Too Low")
        else:
             print(" You Guess the Correct Number ")
             break
    except ValueError :
        print("Invalid Value ")
    attempts-=1
    print(f"Attempts left = {attempts}")
if attempts == 0:
    print(" You Lose ")
    print(f"Number is {num}")
