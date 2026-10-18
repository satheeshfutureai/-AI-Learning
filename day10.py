def greet_ai(name):
    print(f"Hello{name},I am your AI Assistant!")

def add_skill(skill_list,new_skill):
    skill_list.append(new_skill)
    print(f"Skill'{new_skill}' added!")

greet_ai("Satheesh") 

my_skills=["Python"]
add_skill(my_skills,"AI")
add_skill(my_skills,"Machine Learning")

print(f"\nFinaln Skills:{my_skills}")

def check_level(skill_count):
    if skill_count<3:
        return "Beginner"
    elif skill_count<5:
        return "Intermediate"
    else:
        return "Pro"

level=check_level(len(my_skills))
print(f"You are:{level} Level")