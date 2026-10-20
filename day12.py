print("Hey! Na un AI Assistant da!")
name=input("Un peru enna da?").strip()

print(f"\nSemma da{name}! Unna meet pannathula santhosam da !")

while True:
    user_msg = input(f"\n{name} sollu da (exit nu type pana mudiyum):")

    if user_msg.lower() == "exit":
        print(f"Ok da {name},aprom paakalam! Bye da!")
        break
    elif "how are you" in user_msg.lower():
        print("Nalla irukken da ! Nee epdi irukka?")
    elif "your name" in user_msg.lower():
        print("En peru AI Assistant da, un friend")
    elif "python" in user_msg.lower():
        print("Python as semma language da! AI ku king!")
    else:
        print(f"Nee sona '{user_msg}' na purinjukitten da ! Innum sollu!")     