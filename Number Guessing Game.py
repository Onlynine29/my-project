import random
print("welcome to number guessing game")
level = input("select easy or hard:").lower()
if level == "easy":
  print("you have 10 attempts left to guess the number")
  attempts = 10

elif level == "hard" :
 print("you have 5 attemmpts left to guess the number")
 attempts = 5

else:
 print("invalid syntax")
 exit()
number = random.randint(1,50)

while attempts > 0:
   try:
        guess = int(input("guess the number:"))
   except ValueError:
    print("please enter a valid number")
   continue
   if guess > number:
     print("guess was too high")
     attempts -= 1
   elif guess < number:
     print("guess was too low..")
     attempts -= 1
   else:
     print("your guess was right")
     break
   if attempts > 0:
     print(f"you have {attempts} attempts left")
   else:
     print(f"out of attempts, correct number was {number}")