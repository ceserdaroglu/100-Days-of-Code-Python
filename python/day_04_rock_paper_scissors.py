import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game=[rock,paper,scissors]
#Write your code below this line 👇
your_choice=input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ---> ")
if your_choice == "0":
    print(f"You Choose: {rock}")
elif your_choice == "1":
    print(f"You Choose: {paper}")
else:
    print(f"You Choose: {scissors}")

computer_choice= random.choice(game)
print(f"Computer Choose : {computer_choice} ")

if your_choice == "0" and computer_choice == game[2] or your_choice == "1" and computer_choice==game[0] or your_choice=="2" and computer_choice==game[1]:
    print("You Win!")
elif your_choice == "0" and computer_choice==game[1] or your_choice =="1" and computer_choice==game[2] or your_choice=="2" and computer_choice==game[0]:
    print("Haha, you lose. I Win!")
else:
    print("Draw...")