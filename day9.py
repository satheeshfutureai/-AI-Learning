my_ai={"name":"Gayathri AI",
       "age": 19,
       "skills":["Python","AI"],
       "is_learning": True}
print(f"AI Name:{my_ai['name']}")
print(f"Age:{my_ai['age']}")

my_ai["level"]= "Beginner"
print(f"Level:{my_ai['level']}")

print("\n=== Full Profile===")
for key,value in my_ai.items():
    print(f"{key}:{value}")