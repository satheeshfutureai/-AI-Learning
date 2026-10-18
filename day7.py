import random

print("=== AI Number Gusser ===")

ai_number =  random.randint(1,100)
print(f"AI picked a secret number between 1 to 100!")

for i in range(3):
    guess = int(input(f"Chance {i+1}/3 - Guess the number:"))

    if guess == ai_number:
        print("Correct da! You beat the AI!")
        break
    else:
        print("Wrong da, try again!")
else:
    print(f"Game Over! AI number was{ai_number}")        