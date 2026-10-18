ai_assistant ={
    "name": "Satheesh AI",
    "skills": ["Python"],
    "level": "Beginner"
}

def greet():
    print(f"Hi! I am {ai_assistant['name']}")
    print(f"My Level: {ai_assistant['level']}")

def add_new_skill(skill):
    ai_assistant["skills"].append(skill)
    print(f"Learned new skilll: {skill}")

def show_profile():
    print("\n=== MY AI PROFILE===")
    for key,value in ai_assistant.items():
        print(f"{key}:{value}")

        count=len(ai_assistant["skills"])
        if count<3:
            ai_assistant["level"] = "Beginner"
        elif count<5:
            ai_assistant["level"] = "Intermediate"
        else:
            ai_assistant["level"] = "Pro"
        print(f"Skills count:{count}")

#---Main Program---
greet()
add_new_skill("AI")
add_new_skill("Machine Learning")
add_new_skill("Data Science")
show_profile()
greet()                     
          