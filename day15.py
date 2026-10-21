import json
import os

MEMORY_FILE = "memory.json"

if os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "r") as f:
        memory = json.load(f)
    print(f"Nyabagam irukku da: {memory}")
else:
    memory = {}
    print("Puthu AI da!")

if "likes" not in memory:
    memory["likes"] = []

print("List Memory AI Ready da!")

while True:
    msg = input("\nNee sollu da(exit to stop):").strip().lower()

    if msg == "exit":
        with open(MEMORY_FILE, "w") as f:
            json.dump(memory, f)
        print(f"Save pannitten da:{memory}")
        print("Bye da!")
        break

    elif "i like" in msg:
        like = msg.replace("i like", "")
        memory["likes"].append(like)
        print(f"Super da! {like} pudikkum nu save pannitten!")

    elif "what do i like" in msg:
        if memory["likes"]:
            print(f"Unakku ithu ellam pudikkum da: {', '.join(memory['likes'])}")
        else:
            print("Onnum theyriyala da!")

    elif "show memory" in msg:
        print(memory)              
