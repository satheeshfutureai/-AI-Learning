import json
import os

MEMORY_FILE = "memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
    print(f"🧠 Pazhaya nyabagam irukku da: {memory}")
else:
    memory = {}
    print("Puthu AI da, memory empty!")

print("Permanent Memory AI Ready da!")

while True:
    msg = input("\nNee sollu da (exit to stop): ").strip().lower()

    if msg == "exit":
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f)
        print(f"Memory file la save pannitten da: {memory}")
        print("Bye da! Inime marakkave matten!")
        break

    elif "my name is" in msg:
        name = msg.replace("my name is", "").strip()
        memory["name"] = name
        print(f"Ok da {name}, permanent ah save pannitten da!")

    elif "what is my name" in msg:
        if "name" in memory:
            print(f"Un peru {memory['name']} da! Marakkave illa!")
        else:
            print("Peru theriyala da, sollu da!")

    elif "show memory" in msg:
        print(f"En kitta irukka memory: {memory}")

    else:
        print("Solli kudu da!")