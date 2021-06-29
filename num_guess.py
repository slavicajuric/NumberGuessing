import random

print("hello, welcome to my  game! ")

top_of_range= input("type a number: ")
if top_of_range.isdigit():
  top_of_range= int(top_of_range)
  if top_of_range <= 0:
    print("please, type a number greater than 0.")
  quit()


else:
  print("please, put a number next time...")

random_number = random.randint(0, top_of_range)

guesses = 0

while True:
  guesses += 1
  user_guess = input("make a guess: ")
  if user_guess.isdigit():
    user_guess = int(user_guess)
  else:
    print("please type a number next time. ")
    continue 

    if user_guess == random_number:
      print("great, you got it")
      break 
    elif user_guess > random_number:
      print("you are above the number")
    else:
      print("you are below number. ") 
