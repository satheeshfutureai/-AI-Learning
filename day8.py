my_skills =["Python","AI","Problem Solving"]
print("My Skills:",my_skills)

my_skills.append("Machine Learning")
print("After Learning:",my_skills)

print(f"First skills: {my_skills[0]}")
print(f"Last skills: {my_skills[-1]}")

print("\n=== AI is checking your skills===")
for skills in my_skills:
    print(f"Learning {skills}...Done!")

print(f"\nTotal skills you have: {len(my_skills)}")    