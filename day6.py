def check_ai_power(age):
    if age < 18:
        return "Younger Learner - Future is yours!"
    elif age >= 18 and age <= 25:
        return "Peak Learning Age - Best time to master AI!"
    else:
        return "Experienced - You can tech AI!"

print("=== AI Age Analyzer ===")
user_age=int(input("Enter your age:"))

result=check_ai_power(user_age)

print(f"\nYour Age: {user_age}")
print(f"AI Analysis: {result}")

for i in range(3):
    print(f"Motivation {i+1} Keep going satheesh!")