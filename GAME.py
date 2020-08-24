import random 
list1 = ['stone' , 'paper' , 'scissors']
chance = 5
no_of_chances = 0
computer = 0
name2 = 0

print("\t\t\t\t\t\tSTONE PAPER SCISSORS GAME\n\n")
name1 = input("ENTER YOUR NAME\n\n")
while no_of_chances<chance:
    
    imp1 = input("\nSTONE , PAPER OR SCISSORS\n\n")
    random1 = random.choice(list1)

    if imp1 == random1:
        # computer = computer + 0 
        print(f"COMPUTER = {random1}\n{name1} = {imp1}")
        print(f"IT'S A TIE !!\n\nCOMPUTER ={computer}\n{name1} ={name2}\n\n")
    
    elif imp1 == "stone" and random1 == "paper":
        computer = computer + 1
        print(f"COMPUTER = {random1}\n{name1} = {imp1}")
        print(f"COMPUTER WINS 1 POINT !!\n\nCOMPUTER = {computer}\n{name1} = {name2}\n\n")

    elif imp1 == "stone" and random1 == "scissors":
        name2 = name2 + 1
        print(f"COMPUTER = {random1}\n{name1} = {imp1}")
        print(f"{name1} WINS 1 POINT !!\n\nCOMPUTER = {computer}\n{name1} = {name2}\n\n")

    elif imp1 == "paper" and random1 == "scissors":
        computer = computer + 1
        print(f"COMPUTER = {random1}\n{name1} = {imp1}")
        print(f"COMPUTER WINS 1 POINT !!\n\nCOMPUTER = {computer}\n{name1} = {name2}\n\n")

    elif imp1 == "paper" and random1 == "stone":
        name2 = name2 + 1
        print(f"COMPUTER = {random1}\n{name1} = {imp1}")
        print(f"{name1} WINS 1 POINT !!\n\nCOMPUTER = {computer}\n{name1} = {name2}\n\n")

    elif imp1 == "scissors" and random1 == "stone":
        computer = computer + 1
        print(f"COMPUTER = {random1}\n{name1} = {imp1}")
        print(f"COMPUTER WINS 1 POINT !!\n\nCOMPUTER = {computer}\n{name1} = {name2}\n\n")

    elif imp1 == "scissors" and random1 == "paper":
        name2 = name2 + 1
        print(f"COMPUTER = {random1}\n{name1} = {imp1}")
        print(f"{name1} WINS 1 POINT !!\n\nCOMPUTER = {computer}\n{name1} = {name2}\n\n")
        continue

    elif imp1 != list1:
        print(f"DEAR {name1}, PLEASE ENTER A VALID INPUT !!\n")


    no_of_chances = no_of_chances + 1
    print(f"{chance - no_of_chances} chances are left out of {chance} chances\n")
print("GAME OVER\n") 

if name2>computer:
    print(f"CONGRATS {name1} YOU WON !!\n")
elif name2==computer:
    print("IT'S A TIE !!\n")
else:
    print(f"WE ARE SORRY TO SAY {name1}, YOU LOST THIS MATCH AGAINST OUR COMPUTER !!\n")
print(f"FINAL RESULTS :\n\n{name1} ={name2}\nCOMPUTER = {computer}\n\n")
input("Type BYE to exit\n")